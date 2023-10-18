<template>
    <NuxtLayout name="default">
        <div class="padding-16">
          <v-sheet
            class="d-flex align-center flex-column"
            height="200"
          >
            <v-card-actions class="justify-center">
              <h2>{{ survey.name }}</h2>
            </v-card-actions>
            <v-card-actions class="justify-center">
              <p>{{ survey.description }} </p>
            </v-card-actions>
            <v-card-actions class="justify-center">
              <p>Publish date: {{ formatDate(survey.publish_date) }}</p>
            </v-card-actions>
            <v-card-actions class="justify-center">
              <p>Expire date: {{ formatDate(survey.expire_date) }}</p>
            </v-card-actions>
            <v-card-actions class="justify-center" >
              <v-btn @click="createResponse" color="primary">
                <i class="fa-solid fa-play"></i>
                <span class="q-pa-sm">Start survey</span>
              </v-btn>
            </v-card-actions>
          </v-sheet>
            <!-- <p>Counter: {{this.$store.state.counter}}</p>-->
<!--            <h2>{{ survey.name }}</h2>-->

<!--            <p>{{ survey.description }} </p>-->
<!--            <p>Publish date: {{ formatDate(survey.publish_date) }}</p>-->
<!--            <p>Expire date: {{ formatDate(survey.expire_date) }}</p>-->

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

const storeResponse = useStoreResponse()
const survey_url = "/api/surveys/"
const create_response_url = "/api/responses/"
const origin_url = "http://localhost:3000"
const data = ref([])
const route = useRoute()

const survey = await storeResponse.getResponse({ id: route.params._id })

const createResponse = async () => {
    // Make a POST request to your Django API endpoint to create a new Response object
    const respondentId = await storeResponse.createResponse({ id: route.params._id })

    if (respondentId) {
        // Navigate to the /survey/${survey.id}/1 page after the response is created
        return navigateTo('/survey/' + route.params._id + '/1')
    }
}

</script>

