<template>
    <NuxtLayout name="default">


        <div class="q-pa-md row items-start q-gutter-md">
            <!-- Question card: number & text -->
            <q-card class="my-card">
                <q-card-section>
                    <div class="text-h2 q-mt-sm q-mb-xs">Question {{ $route.params._question }}</div>
                    <div class="text-h5 q-mt-sm q-mb-xs">{{ question.text }}</div>
                </q-card-section>
            </q-card>
        </div>

        <div class="q-pa-md row items-start q-gutter-md">
            <!-- Map card
          real v-if statement = (question.map_view != null || question.is_geospatial)-->
            <q-card v-if="question.is_geospatial" style="min-width: 300px;" class="my-card col">
                <q-card-section>
                    <div class="text-h5 q-mt-sm q-mb-xs">Map here</div>
                    <div id="map"></div>
                </q-card-section>
            </q-card>

            <!-- Answer card-->
            <q-card style="min-width: 300px;" class="my-card col">
                <q-card-section>

                </q-card-section>
            </q-card>
        </div>


        <!-- Navigation -->
        <div class="q-pa-md row">
            <q-btn @click="prevQuestion" color="primary">
                <i class="fa-solid fa-arrow-left"></i>
                <!-- <span class="q-pa-sm">Previous</span> -->
            </q-btn>
            <q-space />
            <q-btn @click="nextQuestion" color="primary">
                <i class="fa-solid fa-arrow-right"></i>
                <!-- <span class="q-pa-sm">Next</span> -->
            </q-btn>
        </div>

    </NuxtLayout>
</template>


<script setup>
import { ref } from "vue"
import { navigateTo } from "nuxt/app";
import leaflet from "leaflet"
/**
 * All `/api/**` are proxies pointing to the local or production server of the backend.
 */
const survey_url = "/api/surveys/"
const question_url = "/api/questions/"
const data = ref([])
const route = useRoute()

const { data: survey } = await useAsyncData(() => $cmsApi(survey_url + route.params._id));

// TODO: use an API to get n'th question of the selected survey
// for demo only, I will use (5 + question id).
let demo_question = parseInt(route.params._question, 10) + 5
let { data: question } = await useAsyncData(() => $cmsApi(question_url + demo_question));

const prevQuestion = async () => {
    // if this is not the first question:
    let question_to_navigate = (parseInt(route.params._question, 10) - 1)
    if (question_to_navigate != 0) {
        return navigateTo('/survey/' + route.params._id + '/' + question_to_navigate)
    } else {
        return navigateTo('/survey/' + route.params._id)
    }
}

const nextQuestion = async () => {
    // if this is not the last question:
    return navigateTo('/survey/' + route.params._id + '/' + (parseInt(route.params._question, 10) + 1))
}


</script>

<style lang="scss">
#map {
    height: 180px;
}
</style>
