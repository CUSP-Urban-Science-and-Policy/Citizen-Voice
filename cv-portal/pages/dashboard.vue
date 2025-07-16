<template>
    <v-app>
        <HeaderCVPortal />
        <v-main class="pt-0 relative block">
            <div class="z-10">
                <MapDashboard :zoom="options.zoom" :center="options.center" :filteredFeatures="filteredFeatures"
                    :features="features" />
            </div>
            <div class="absolute z-20 top-[42px] left-[42px]">
                <div
                    class="w-[301px] h-auto p-3 bg-white rounded-[10px] shadow-[0px_1px_3px_0px_rgba(0,0,0,0.30)] flex-col justify-start items-start gap-2 inline-flex overflow-hidden">
                    <div class="h-[21px] relative" @click="toggleLegend()">
                        <div
                            class="left-0 top-[1px] absolute text-black text-xl font-semibold font-['Chillax'] leading-tight tracking-wide">
                            Legend
                        </div>
                        <div data-svg-wrapper class="left-[257px] top-0 absolute cursor-pointer">
                            <svg width="22" height="22" viewBox="0 0 22 22" fill="none"
                                xmlns="http://www.w3.org/2000/svg">
                                <path
                                    d="M2.11111 13.2222H8.77778M8.77778 13.2222V19.8889M8.77778 13.2222L1 21M19.8889 8.77778H13.2222M13.2222 8.77778V2.11111M13.2222 8.77778L21 1"
                                    stroke="#C5C5BA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                            </svg>
                        </div>
                    </div>
                    <ul v-if="!clapsLegend" class="flex-col justify-start items-start gap-2 inline-flex">
                        <li v-for="topic in topics" :key="topic.id"
                            class="justify-start items-center gap-3 flex overflow-hidden p-[2px]">
                            <input :id="`checkbox-${topic.id}`" type="checkbox" :checked="topic.checked"
                                @change="updateChecked(topic.id)"
                                class="w-4 h-4 focus:rounded-lg focus:ring-blue-500 focus:ring-2 relative" />
                            <img v-if="topic?.name" :class="[
                                'btn-w-[26px] h-[26px] rounded-full p-[1px]',
                                images[topic.name.toLowerCase().split(' ').join('-')] && `icon-${topic.name.toLowerCase().split(' ').join('-')}`,
                            ]" :src="images[topic.name.toLowerCase().split(' ').join('-')]" />

                            <label :for="`checkbox-${topic.id}`" class="cursor-pointer">
                                {{ topic.name }}
                            </label>
                        </li>
                    </ul>
                </div>
            </div>

        </v-main>
        <FooterCVPortal />
    </v-app>
</template>

<script lang="ts" setup>
import { filename } from 'pathe/utils'
import { isEmpty, pathOr, is, last, pipe, andThen, find, propOr, propEq } from 'ramda';
import type {
    components,
} from '#nuxt-api-party/cmsApiV1'
import type {
    components as componentsCms,
} from '#nuxt-api-party/cmsApiV3'

const glob = import.meta.glob('@/assets/icons/*.png', { eager: true })
const images = Object.fromEntries(
    Object.entries(glob).map(([key, value]) => [filename(key), (value as any).default])
)

type Answer = components['schemas']['Answer']
type Topic = componentsCms['schemas']['Topic']
type Question = componentsCms['schemas']['Question']

type TopicExtended = {
    checked?: boolean;
} & Topic;

interface Feature {
    properties: {
        question: string,
        topic: TopicExtended
    }
}

const options = ref({
    zoom: 14,
    center: [52.0070404449157, 4.369566115129942]
})
const topics = ref<TopicExtended[]>([])
const filteredFeatures = ref<Feature[]>([])
const features = ref<Feature[]>([])
const clapsLegend = ref(false)

definePageMeta({
    layout: false
})

async function asyncMapFetch<T>(dataArray: T[], urlKey: string | string[], appendBool: boolean = false) {
    // Map over the array and create an array of promises
    const fetchPromises = dataArray.map(async (item: T) => {
        const newKeyName = is(String, urlKey) ? urlKey : last(urlKey)
        // @ts-expect-error we don't know the key yet
        const url = pathOr(item[urlKey], urlKey, item);

        if (!url) {
            // If no URL found, return empty array
            return item;
        }

        try {
            const response = await fetch(url);

            // Check if response is OK (status 200-299)
            if (!response.ok) {
                return item;
            }

            const data = await response.json();

            if (appendBool) {
                return data ? { ...item, [`${newKeyName}Data`]: data } : { ...item };
            }

            // Return fetched data or empty array if no data
            return data
        } catch (error) {
            // On fetch or parsing error, return empty array
            console.log('Error fetch: ', error)
            return [];
        }
    });

    // Wait for all fetches to complete
    return Promise.all(fetchPromises);
}

onMounted(async () => {
    // Fetch topics
    try {
        const topicsData = await $cmsApiV3('/voice/v3/topics/')
        if (topicsData) {
            topics.value = topicsData.map((topic: TopicExtended) => ({ ...topic, checked: true }))
        } else {
            console.error('No topics data received')
        }
    } catch (error) {
        console.log(error)
    }
    // Fetch answers
    try {
        const answersData: Answer[] = await $cmsApiV3('/voice/v3/answers/', {
            // @ts-expect-error some how typscript does not recognize the 'query' parameter
            query: {
                survey: 3
            },
        })

        const updatedAnswersData = await pipe(
            async data => await asyncMapFetch<Answer>(data, 'question', true),
            andThen(async data => await asyncMapFetch<Answer>(data, 'mapview', true)),
            andThen(async data => await asyncMapFetch<Answer>(data, ['mapviewData', 'location'], true)),
        )(answersData);

        if (!isEmpty(answersData)) {
            const featuresSerialized = updatedAnswersData
                .map((answer) => {
                    const feature = pathOr([], ['locationData', 'geojson'], answer)

                    // Get topic id
                    const relatedTopic = pathOr<string | null>(null, ['questionData', 'topics', 0], answer)
                    const relatedTopicId = is(String, relatedTopic)
                        ? Number(relatedTopic.split("/").slice(-2, -1)[0])
                        : null;
                    // get Topic Object
                    const relatedTopicProperties = relatedTopicId ? find(propEq(relatedTopicId, 'id'))(topics.value) : null

                    if (!isEmpty(feature) && is(Object, feature)) {
                        // Add a new property to each feature's properties using map
                        // eslint-disable-next-line @typescript-eslint/no-explicit-any
                        const updatedFeatures = (feature as any).features.map((feature: { properties: any }) => ({
                            ...feature,
                            properties: {
                                ...feature.properties,
                                question: answer?.questionData?.text,
                                topic: relatedTopicProperties
                            }
                        }));

                        return updatedFeatures
                    } else {
                        console.log(
                            'Invalid feature data for answer:',
                            answer
                        )
                        return null
                    }
                })
                .filter((feature) => feature !== null)
            features.value = [].concat(...featuresSerialized)
        } else {
            console.error('No answers data received')
        }
    } catch (error) {
        console.log('answersData ' + error)
    }
})

const activeTopics = computed(
    () => topics.value.filter(item => item.checked).map(item => item.id)
)

const updateChecked = (id: number) => {
    const topic = topics.value.find(t => t.id === id)
    if (topic) {
        topic.checked = !topic.checked
    }

    filteredFeatures.value = features.value.filter(item => {
        if (!item.properties?.topic) return true // Let's return this for now or else they won't be visisble

        return activeTopics.value.includes(item.properties.topic.id)
    })
}

const toggleLegend = () => {
    clapsLegend.value = !clapsLegend.value
}

</script>

<style scoped>
.padding-16 {
    padding: 16px;
}

input[type='checkbox'] {
    width: 20px;
    height: 20px;
    appearance: none;
    -webkit-appearance: none;
    border: transparent;
    cursor: answers;
    position: relative;
}

input[type='checkbox'] {
    content: '';
    background-image: url("data:image/svg+xml, %3Csvg width='20' height='20' viewBox='0 0 20 20' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Crect x='0.5' y='0.5' width='19' height='19' rx='5.5' fill='white' /%3E%3Crect x='0.5' y='0.5' width='19' height='19' rx='5.5' stroke='%23C5C5BA' /%3E%3C/svg%3E");
}

input[type='checkbox']:checked::after {
    content: '';
    position: absolute;
    left: 0px;
    top: 0px;
    width: 20px;
    height: 20px;
    background-image: url("data:image/svg+xml,%3Csvg width='20' height='20' viewBox='0 0 20 20' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Crect x='0.5' y='0.5' width='19' height='19' rx='5.5' fill='white' /%3E%3Crect x='0.5' y='0.5' width='19' height='19' rx='5.5' stroke='black' /%3E%3Cpath d='M14.6666 6.5L8.24998 12.9167L5.33331 10' stroke='black' stroke-width='2' stroke-linecap='round' stroke-linejoin='round' /%3E%3C/svg%3E");
    background-position: 0%;
    background-repeat: no-repeat;
}

input[type='checkbox']~* {
    color: hwb(60 50% 47%);
    font-size: 1rem;
    font-weight: 400;
    font-family: 'Chillax';
    line-height: 18px;
    line-height: 18px;
    letter-spacing: 0.05em;
}

input[type='checkbox']+img {
    opacity: 0.4;
    filter: alpha(opacity=40);
}

input[type='checkbox']:checked~label {
    color: #000;
}

input[type='checkbox']:checked~img {
    opacity: 1;
    filter: none;
}
</style>
