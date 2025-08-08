<template>
    <NuxtLayout name="default">
        <div class="flex flex-row">
            <h2 class="inline-block">Surveys</h2>
            <v-btn variant="outlined" href="/design/surveys/create">Add
                survey</v-btn>
        </div>

        <v-card v-if="surveys">
            <v-list>
                <v-list-item :link="false" v-for="(item, i) in surveys" :key="i" :value="item">
                    <template v-slot:prepend>
                        <v-btn color="dark" variant="plain" :href="`/design/surveys/${item.id}`" icon="mdi-file">
                        </v-btn>
                    </template>

                    <template v-slot:append>
                        <div>
                            <v-btn color="dark" variant="plain" @click="deleteHandler(item.id)" icon="mdi-delete">
                            </v-btn>
                            <v-btn color="dark" variant="plain" :href="`/design/surveys/${item.id}`"
                                icon="mdi-dots-vertical">
                            </v-btn>
                        </div>
                    </template>

                    <v-list-item-title>{{ item.name }} | #{{ item.id }}</v-list-item-title>
                </v-list-item>
            </v-list>
        </v-card>

    </NuxtLayout>
</template>

<script setup>
import { ref } from 'vue'
import BaseButton from "~/components/BaseButton";
import ListItemSurveyDesign from "~/components/ListItemSurveyDesign";
import { formatDate } from "~/utils/formatData"
import { useSurveyStore } from "~/stores/survey"

// Make sure the user is authenticated or trigger the reroute to login
definePageMeta({
    middleware: 'authorization',
    alias: '/design/surveys'
})

const surveyStore = useSurveyStore()

var expire_date = new Date();
var current_date = new Date();
const textName = ref(null)
const textDescription = ref(null)

// set default expire date 100 days after current day
expire_date.setDate(expire_date.getDate() + 100);
current_date.setDate(current_date.getDate());

let response = ref({})
let refresh = ref(() => { })
let surveys = ref([])

onMounted(async () => {
    const response_ = await surveyStore.getSurveysOfCurrentUser()
    response.value = response_
    surveys.value = response_.data.value
});

// Add a new survey using the surveyStore, based on what is entered in the field.
const addNewSurvey = async () => {
    await surveyStore.createSurvey(textName.value, textDescription.value, current_date, expire_date)
}

const deleteHandler = async (id) => {
    console.log('id //> ', id)
    // DELETE request using the surveyStore with error handling
    await surveyStore.deleteSurvey(id)
    refresh()
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

.custom-width-60-pc {
    width: 60%;
}

.padding-16 {
    padding: 16px;
}

.button {
    margin-left: 24px;
}
</style>
