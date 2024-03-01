<template>
  <!-- Survey/index.vue -->
    <NuxtLayout name="default">
        <div class="padding-16">
          <v-sheet
            class="d-flex align-center flex-column"
            height="200"
          >
          <v-card 
            class="my-card" 
            :title=survey.name
            :subtitle="'Open until:' + formatDate(survey.expire_date)"   
            :text="survey.description"
            >
            <v-card-actions class="justify-center" >
              <v-btn @click="startSurvey" color="primary"  variant="elevated">
                <i class="fa-solid fa-play"></i>
                <span class="q-pa-sm">Start Survey</span>
              </v-btn>
            </v-card-actions>
          </v-card>
          </v-sheet>
            <!-- <p>Counter: {{this.$store.state.counter}}</p>-->
            <!-- <h2>{{ survey.name }}</h2> -->
<!--            <h2>{{ survey.name }}</h2>-->

            <!-- <p>{{ survey.description }} </p> -->
            <!-- <p>Publish date: {{ formatDate(survey.publish_date) }}</p> -->
            <!-- <p>Expire date: {{ formatDate(survey.expire_date) }}</p> -->
<!--            <p>{{ survey.description }} </p>-->
<!--            <p>Publish date: {{ formatDate(survey.publish_date) }}</p>-->
<!--            <p>Expire date: {{ formatDate(survey.expire_date) }}</p>-->

            <!-- <v-btn @click="createResponse" color="primary"> -->
                <!-- <i class="fa-solid fa-play"></i> -->
                <!-- <span class="q-pa-sm">Start survey</span> -->
            <!-- </v-btn> -->
<!--            <v-btn @click="createResponse" color="primary">-->
<!--                <i class="fa-solid fa-play"></i>-->
<!--                <span class="q-pa-sm">Start survey</span>-->
<!--            </v-btn>-->

            <!--{{ $route.params.id }}
                <pre>{{ survey }}</pre> -->
        </div>
    </NuxtLayout>
</template>

<script setup>
import { ref } from "vue"
import { navigateTo } from "nuxt/app";
import { useStoreResponse } from '~/stores/response'
import { useSurveyStore } from '~/stores/survey'
const storeResponse = useStoreResponse()
const survey_url = "/api/surveys/"
const create_response_url = "/api/responses/"
const origin_url = "http://localhost:3000"
const data = ref([])
const route = useRoute()
console.log('route id', route.params._id)
const survey = await storeResponse.getSurvey({ id: route.params._id })
console.log('survey.value. in survey index //', survey.value.id)
const storeSurvey = useSurveyStore()

// Clear all answers in the Response store
storeResponse.clearAnswers()

const createResponse = async () => {
    // Make a POST request to your Django API endpoint to create a new Response object
    // await storeResponse.createResponse({ id: route.params._id })
    const responseId = await storeResponse.createResponse({ surveyId: survey.value.id, respondentId: 1 })
    
    // Navigate to the /survey/${survey.id}/1 page after the response is created
    if (responseId) {

      console.log('response id //', responseId)
        // Navigate to the /survey/${survey.id}/1 page after the response is created
        return navigateTo('/survey/' + route.params._id )
    }

};

const getQuestions = async () => {
    // Make a GET request to your Django API endpoint to get the questions for the survey
    const questions = await storeSurvey.getQuestionsOfSurvey()
    console.log('questions //', questions)
    // Navigate to the /survey/${survey.id}/1 page after the response is created
    // if (questions) {
    //     // Navigate to the /survey/${survey.id}/1 page after the response is created
    //     return navigateTo('/survey/' + route.params._id + '/' + survey.value.id)
    // }
    return questions
};

const startSurvey = async () => {
  await createResponse();
  const questions = await getQuestions();
  
  if (questions) {
    // Navigate to the /survey/${survey.id}/1 page after the response is created
    return navigateTo('/survey/' + survey.value.id + '/' + 1 ) // TODO: replace 1 with  question orden
}
};


</script>