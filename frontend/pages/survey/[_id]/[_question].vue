<template>
    <NuxtLayout v-if="respondentId" name="default">
        <client-only placeholder="Loading...">
            <div class="">
                <question-header v-if="(questions.length > current_question_index)" :question_index="current_question_index"
                    :question="questions[current_question_index]"></question-header>
                <component
                    v-if="(questions.length > current_question_index) && questions[current_question_index].question_type"
                    :is="answerTypes[questions[current_question_index].question_type.replace('_', '-')].comp"
                    :question_index="current_question_index" :question="questions[current_question_index]"
                    :answer="answers[current_question_index]"
                    @updateAnswer="(answer, index) => updateAnswers(answer, index)">
                </component>
                <!--            <h2>{{current_question_index}}</h2>-->
                <!--            <h1 v-for="answer in answers">{{answer}}</h1>-->
                <!--          <h2>{{questions[current_question_index]}}</h2>-->
            </div>
            <!-- Navigation -->
            <div class="d-flex flex-row mb-6 justify-end" v-if="current_question_index < questions.length">
                <v-layout class="justify-center">
                    <v-card-actions>
                        <v-btn class="" @click="prevQuestion" color="primary">
                            <v-icon dark left>mdi-arrow-left</v-icon>
                            <i class="fa-solid fa-arrow-left"></i>
                            <span class="q-pa-sm">Previous Question</span>
                        </v-btn>
                    </v-card-actions>
                    <v-card-actions>
                        <v-btn class="" @click="nextQuestion" color="primary">
                            <i class="fa-solid fa-arrow-right"></i>
                            <span class="q-pa-sm">Next Question</span>
                            <v-icon dark left>mdi-arrow-right</v-icon>
                        </v-btn>
                    </v-card-actions>
                </v-layout>
            </div>
            <end-survey v-if="questions.length === current_question_index" @returnToSurvey="(props) => backToSurvey()"
                @finishSurvey="(props) => submitSurvey()"></end-survey>



            <!--        <div v-if="(questions.length > current_question_index)">-->
            <!--          <div class="q-pa-md row items-start q-gutter-md">-->
            <!--              &lt;!&ndash; Map card &ndash;&gt;-->
            <!--              <div v-show="(question.map_view != null || question.is_geospatial)" style="min-width: 600px;"-->
            <!--                  class="my-card col">-->
            <!--                  <div style="height:300px; width:600px">-->
            <!--                      <l-map ref="map" v-model:zoom="map_view.options.zoom" :center="map_view.options.center" :minZoom="1"-->
            <!--                          :maxZoom="18" @click="addCircle">-->
            <!--                          <l-tile-layer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" layer-type="base"-->
            <!--                              name="OpenStreetMap"></l-tile-layer>-->
            <!--                          <l-circle v-for="circle, index in map_view.options.points" :lat-lng="circle"-->
            <!--                              :radius="map_view.options.radius" :color="map_view.options.color"-->
            <!--                              :fillColor="map_view.options.fillColor"></l-circle>-->
            <!--                          <l-circle v-for="circle, index in circles" @click="removeCircle(index)" :lat-lng="circle"-->
            <!--                              :radius="map_view.options.radius" :color="map_view.options.color"-->
            <!--                              :fillColor="map_view.options.fillColor"></l-circle>-->
            <!--                          <l-control position="bottomleft">-->
            <!--                              <v-btn @click="resetMap">-->
            <!--                                  Reset-->
            <!--                              </v-btn>-->
            <!--                          </l-control>-->
            <!--                      </l-map>-->
            <!--                  </div>-->
            <!--              </div>-->
            <!--=======-->
            <!--            &lt;!&ndash; Question card: number & text &ndash;&gt;-->
            <!--            <v-card v-for="question in questions" class="my-card">-->
            <!--                <div class="text-h2 q-mt-sm q-mb-xs">Question {{ question.order }}</div>-->
            <!--                <div class="text-h5 q-mt-sm q-mb-xs">{{ question.text }}</div>-->
            <!--            </v-card>-->


            <!--            <div class="">-->
            <!--                &lt;!&ndash; Map card-->
            <!--          real v-if statement = (question.map_view != null || question.is_geospatial)&ndash;&gt;-->
            <!--                &lt;!&ndash;            <v-card v-if="question.is_geospatial" style="min-width: 300px;" class="my-card col">&ndash;&gt;-->
            <!--                &lt;!&ndash;                <div class="text-h5 q-mt-sm q-mb-xs">Map here</div>&ndash;&gt;-->
            <!--                &lt;!&ndash;                <div id="map"></div>&ndash;&gt;-->
            <!--                &lt;!&ndash;            </v-card>&ndash;&gt;-->
            <!--            </div>-->

            <!--            <div class="my-card">-->
            <!--                <div class="text-h2 q-mt-sm q-mb-xs">Question {{ $route.params._question }}</div>-->
            <!--                <div class="text-h5 q-mt-sm q-mb-xs">{{ question.text }}</div>-->
            <!--            </div>-->
            <!--        </div>-->

            <!--        <div class="q-pa-md row items-start q-gutter-md">-->
            <!--            &lt;!&ndash; Map card &ndash;&gt;-->
            <!--            <div v-show="(question.map_view != null || question.is_geospatial)" style="min-width: 600px;"-->
            <!--                class="my-card col">-->
            <!--                <div style="height:300px; width:600px">-->
            <!--                    <l-map ref="map" v-model:zoom="map_view.options.zoom" :center="map_view.options.center" :minZoom="1"-->
            <!--                        :maxZoom="18" @click="addCircle">-->
            <!--                        <l-tile-layer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" layer-type="base"-->
            <!--                            name="OpenStreetMap"></l-tile-layer>-->
            <!--                        <l-circle v-for="circle, index in map_view.options.points" :lat-lng="circle"-->
            <!--                            :radius="map_view.options.radius" :color="map_view.options.color"-->
            <!--                            :fillColor="map_view.options.fillColor"></l-circle>-->
            <!--                        <l-circle v-for="circle, index in circles" @click="removeCircle(index)" :lat-lng="circle"-->
            <!--                            :radius="map_view.options.radius" :color="map_view.options.color"-->
            <!--                            :fillColor="map_view.options.fillColor"></l-circle>-->
            <!--                        <l-control position="bottomleft">-->
            <!--                            <v-btn @click="resetMap">-->
            <!--                                Reset-->
            <!--                            </v-btn>-->
            <!--                        </l-control>-->
            <!--                    </l-map>-->
            <!--                </div>-->
            <!--            </div>-->

            <!--            &lt;!&ndash; Answer card&ndash;&gt;-->
            <!--            <div class="my-card col">-->
            <!--                <v-textarea name="title" v-model="answer_field" type="textarea" label="Give answer here"></v-textarea>-->
            <!--            </div>-->


            <!--        </div>-->

            <!--        &lt;!&ndash; Navigation &ndash;&gt;-->
            <!--        <div class="q-pa-md row">-->
            <!--            <v-btn @click="prevQuestion" color="primary">-->
            <!--                <i class="fa-solid fa-arrow-left"></i>-->
            <!--                <span class="q-pa-sm">Previous Question</span>-->
            <!--            </v-btn>-->
            <!--            <v-space />-->
            <!--            <v-btn @click="nextQuestion" color="primary">-->
            <!--                <i class="fa-solid fa-arrow-right"></i>-->
            <!--                <span class="q-pa-sm">Next Question</span>-->
            <!--            </v-btn>-->
            <!--&gt;>>>>>> upstream/devel-->
            <!--        </div>-->
        </client-only>
    </NuxtLayout>
</template>


<script setup>
import { ref } from "vue"
import { navigateTo } from "nuxt/app";
import { useSurveyStore } from "~/stores/survey.js";
import { useStoreResponse } from '~/stores/response'
// import leaflet from "leaflet"
import "leaflet/dist/leaflet.css";
import { LMap, LTileLayer, LCircle, LControl } from "@vue-leaflet/vue-leaflet";

/**
 * Init stores
 */
const responseStore = useStoreResponse()
const survey_store = useSurveyStore()

const route = useRoute()
// Fixme: Cleanup these functions
import { DATE, INTEGER, SELECT, SELECT_MULTIPLE, TEXT } from "~/constants/questions.js";
import AnswerTypeSelect from "~/components/respondent_view_question_types/AnswerTypeSelect.vue";
import AnswerTypeSelectMultiple from "~/components/respondent_view_question_types/AnswerTypeSelectMultiple.vue";
import AnswerTypeText from "~/components/respondent_view_question_types/AnswerTypeText.vue"
import { Number } from "~/components/question-blocks/index.js";
import Answer from "~/components/respondent_view_question_types/util/answer.js";
import EndSurvey from "~/components/respondent_view_question_types/endSurvey.vue";
import QuestionHeader from "~/components/respondent_view_question_types/util/QuestionHeader.vue";
import AnswerTypeInteger from "~/components/respondent_view_question_types/AnswerTypeInteger.vue";
import AnswerTypeDate from "~/components/respondent_view_question_types/AnswerTypeDate.vue";

const { data: questions } = await survey_store.getQuestionsOfSurvey(route.params._id)
const answers = ref([])
const respondentId = ref(null)
let current_question_index = ref(0)

respondentId.value = responseStore.getRespondentId()

questions.value.forEach(function (item, index) {
    const responseId = 999
    let newAnswer = new Answer(route.params._id, responseId, index)
    answers.value.push(newAnswer)
})

console.log("Questions")
console.log(questions)
console.log("Answers")
console.log(answers)

// =======
// const survey_store = useSurveyStore()
// // const { data: survey } = await useAsyncData(() => $cmsApi(survey_url + route.params._id));
// const { data: questions } = await survey_store.getQuestionsOfSurvey(route.params._id)
// var current_question_index = 0
//
// const survey = await responseStore.getResponse(route.params._id)
//
// >>>>>>> upstream/devel

// // TODO: use an API to get n'th question of the selected survey
// let demo_question = 3 // This is a hardcoded value for now
// let { data: question } = await useAsyncData(() => $cmsApi(question_url + demo_question));
// // TODO: get question.map_view once APIs are configured
// const { data: map_view } = await useAsyncData(() => $cmsApi(mapview_url + 1)); // for demo only, I will use 5th

// onMounted(() => {
//   for (let i = 0; i < questions.length; i++) {
//     responseStore.state.answersToCurrentSurvey.push(answerPlaceholder)
//   }
//   console.log("Answers to current survey")
//   console.log(questions.length)
//   console.log(responseStore.answersToCurrentSurvey)
// })

const circles = ref([]) // this is what user will add
// L.latLng(47.414, -1.22),
// circleClickedAndRemoved is a boolean we use to keep track of whether a circle was just clicked
// if that is the case, we will not call the addCircle function
let circleClickedAndRemoved = false
let resetClicked = false

// created = models.DateTimeField(_("Creation date"))
// updated = models.DateTimeField(_("Last edited"))

const answerPlaceholder = {
    response: Number,
    question: Number,
    created: "",
    updated: "",
    body: "",
}

const answerTypes = {
    [TEXT]: {
        label: 'Text Answer',
        comp: AnswerTypeText,
        type: TEXT
    },
    [SELECT]: {
        label: 'Select Answer',
        comp: AnswerTypeSelect,
        type: SELECT
    },
    [SELECT_MULTIPLE]: {
        label: 'Select Multiple Answer',
        comp: AnswerTypeSelectMultiple,
        type: SELECT_MULTIPLE
    },
    [INTEGER]: {
        label: 'Integer Answer',
        comp: AnswerTypeInteger,
        type: INTEGER
    },
    [DATE]: {
        label: 'Date Answer',
        comp: AnswerTypeDate,
        type: DATE
    },
}

// to navigate from one question to the previous/next
const prevQuestion = async () => {
    console.log("Prev question")
    current_question_index.value -= 1
    current_question_index.value = Math.max(current_question_index.value, 0)
    // console.log(current_question_index.value)
    // TODO: Implement
}
const nextQuestion = async () => {
    console.log("Next question")

    current_question_index.value += 1
    current_question_index.value = Math.min(current_question_index.value, questions.value.length)
    console.log(current_question_index.value)
    console.log(questions.value)
    console.log(questions.value[current_question_index])
    // console.log(answerTypes[questions[current_question_index].question_type.replace('_', '-')])
}

const backToSurvey = () => {
    current_question_index.value = 0
    console.log("return to survey")
}

const submitSurvey = () => {
    console.log("submit survey")
    console.log(answers.value)
    responseStore.submitAnswer(answers.value)
}

const updateAnswers = (answer, index) => {
    answers.value[index] = answer
}

// inspired by Roy J's solution on Stack Overflow:
// https://stackoverflow.com/questions/54499070/leaflet-and-vuejs-how-to-add-a-new-marker-onclick-in-the-map
const removeCircle = async (index) => {
    console.log("removeCircle function called")
    circles._value.splice(index, 1)
    circleClickedAndRemoved = true
}
const addCircle = async (event) => {
    if (circleClickedAndRemoved) {
        circleClickedAndRemoved = false
    } else if (resetClicked) {
        resetClicked = false
    } else {
        console.log("addCircle function called")
        circles._value.push(
            [event.latlng.lat, event.latlng.lng]
        )
    }
}
const resetMap = async () => {
    console.log("resetMap function called")
    circles._value.splice(0, circles._value.length)
    // TODO: reset map center and zoom level based on map_view
    resetClicked = true
}

</script>

<style lang="scss">
#map {
    height: 180px;
}
</style>
