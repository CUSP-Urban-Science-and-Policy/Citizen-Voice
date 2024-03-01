<template>
    <NuxtLayout name="default">
        <client-only placeholder="Loading...">
            <form class="mt-4 flex flex-row" @submit.prevent="saveSurvey">
                <div class="content max-w-3xl ml-auto">
                    <h2 class="mb-4 font-bold">{{ textName || '[ Untitled ]' }}</h2>
                    <v-text-field name="title" v-model="textName" label="Title"></v-text-field>
                    <v-textarea name="title" variant="outlined" v-model="textDescription" type="textarea"
                        label="Description"></v-textarea>
                    <div v-if="route?.params?._id">
                        <h3 class="mb-6">Questions</h3>

                        <draggable h="auto" v-model="questionStore.currentQuestions" item-key="id">
                            <template #item="{ element, index }">
                                <div>
                                    <component :questionIndex="index" v-if="questionTypes[element.question_type]"
                                        :is="questionTypes[element.question_type].comp" v-bind="{ ...element, index }">
                                    </component>
                                </div>
                            </template>
                        </draggable>

                        <v-menu>
                            <template v-slot:activator="{ props }">
                                <v-btn class="cursor-pointer" v-bind="props">
                                    <v-icon>mdi-plus-circle</v-icon> Add Question
                                </v-btn>
                            </template>

                            <v-list>
                                <v-list-item v-for="(item, i) in questionTypes" :key="i" :value="i" @click="addQuestion({
                                    choices: '',
                                    text: '',
                                    survey: survey.id,
                                    order: questionStore.currentQuestions.length + 1,
                                    required: false,
                                    question_type: item.type,
                                    is_geospatial: false,
                                    map_view: null,
                                })">


                                    <v-list-item-title>{{ item.label }}</v-list-item-title>
                                </v-list-item>
                            </v-list>

                        </v-menu>
                    </div>
                </div>
                <aside class="aside">
                    <VBtn variant="outlined" class="me-4" type="submit">
                        Save survey
                    </VBtn>
                </aside>
            </form>
        </client-only>
    </NuxtLayout>
</template>

<script setup>
import { ref } from 'vue'
import { TEXT, SHORT_TEXT, RADIO, SELECT, SELECT_MULTIPLE, FLOAT, DATE } from "~/constants/questions"
import { TextArea, TextShort, Radio, Select, SelectMultiple, Number, Date as DateComp } from "@/components/question-blocks"
import { useSurveyStore } from "~/stores/survey"
import { useQuestionDesignStore } from "~/stores/questionDesign"
import { useMapViewStore } from "~/stores/mapview"
import { pathOr } from 'ramda'

// Init stores

useMapViewStore()
const surveyStore = useSurveyStore()


// Make sure the user is authenticated or trigger the reroute to login
definePageMeta({ middleware: 'authorization' })

/**
 * States
 */

const dragging = ref(false)
const route = useRoute()


const draggingInfo = computed(() => {
    return dragging.value ? "under drag" : "";
});

const questionTypes = {
    [TEXT]: {
        label: 'Text Area',
        comp: TextArea,
        type: TEXT
    },
    [SHORT_TEXT]: {
        label: 'Text Short',
        comp: TextShort,
        type: SHORT_TEXT
    },
    [RADIO]: {
        label: 'Radio Select',
        comp: Radio,
        type: RADIO
    },
    [SELECT]: {
        label: 'Select',
        comp: Select,
        type: SELECT
    },
    [SELECT_MULTIPLE]: {
        label: 'Select Multiple',
        comp: SelectMultiple,
        type: SELECT_MULTIPLE
    },
    [FLOAT]: {
        label: 'Number',
        comp: Number,
        type: FLOAT
    },
    [DATE]: {
        label: 'Date',
        comp: DateComp,
        type: DATE
    },
    // TODO: these are two more question types we might need later but for now leave them out for the MVP
    // [SELECT_IMAGE]: SelectImage,
    // [INTEGER]: Integer,
}




/**
 * Survey
 */


const { data: survey, refresh } = await surveyStore.getSurvey(route.params._id)

var expire_date = new Date();
var current_date = new Date();

const textName = ref(pathOr('', ['value', 'name'], survey))
const textDescription = ref(pathOr('', ['value', 'description'], survey))

// set default expire date 100 days after current day
expire_date.setDate(expire_date.getDate() + 100);
current_date.setDate(current_date.getDate());

/**
 * Questions
 */
const questionStore = useQuestionDesignStore()
if (route?.params?._id) await questionStore.setOrderedQuestionBySurvey(route.params._id)


// Add Question handler
const addQuestion = (item) => {
    questionStore.addNewQuestion(item)
}

// Add a new survey using the surveyStore, based on what is entered in the field.
const saveSurvey = async () => {
    // If the id route exists we can assume that the survey already exists too
    if (route?.params?._id) {
        await surveyStore.updateSurvey(route?.params?._id, {
            name: textName.value,
            description: textDescription.value,
        })
    } else {
        const { id } = await surveyStore.createSurvey(textName.value, textDescription.value, current_date, expire_date)
        navigateTo(`/design/surveys/${id}`)
    }
    await questionStore.saveCurrentQuestions()
}


</script>

<style lang="scss" scoped>
.custom-bg-white {
    background-color: #fff;
}

.custom-list-item {
    //min-height: 50vh;
    height: calc(100vh/3);
    background: #fff;
    overflow: hidden;
    overflow-y: scroll;
}

::-webkit-scrollbar {
    width: 0;
    background: transparent;
    /* make scrollbar transparent */
}

.custom-scroll {
    position: relative;
    max-height: 100%;
    overflow-y: scroll;
}

::-webkit-scrollbar {
    width: 0;
    background: transparent;
    /* make scrollbar transparent */
}

.custom-bg-red {
    min-width: 100%;
    min-height: 100%;
    background: #b02a37;
}

.content {
    width: 100%;
}

.container {
    display: flex;
    max-width: 975px;
    margin: 0 auto;
    padding: 32px 16px;
}

.aside {
    min-width: 200px;
    padding-top: 24px;
    padding-left: 32px;
}

.custom-width-60-pc {
    width: 60%;
}

.input {
    margin-bottom: 24px;
}
</style>
