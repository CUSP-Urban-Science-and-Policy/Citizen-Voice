<template>
    <NuxtLayout name="default">
        <div class="padding-16">
            <h2 class="h2">Surveys</h2>
            <div class="row q-col-gutter-sm">
                <v-card v-for="survey in surveys" style="min-width: 300px;" class="my-card col" flat bordered>
                    <v-card-section class="">
                        <div class="text-h5 q-mt-sm q-mb-xs">{{
                            survey.name
                        }}</div>
                        <p class="text-caption ">
                            {{ survey.description }}
                        </p>
                        <div class=" text-caption">
                            <span>Publish date: {{ formatDate(survey.publish_date) }}</span><br />
                            <span>Expire date: {{ formatDate(survey.expire_date) }}</span>
                        </div>
                        <v-card-actions style="padding-left: 0" margin="0" class="item-end q-mt-auto">
                            <v-btn :to="`/survey/${survey.id}`" color="primary">
                                <i class="fa-solid fa-play"></i>
                                Start survey
                            </v-btn>
                        </v-card-actions>
                    </v-card-section>
                </v-card>
            </div>
        </div>
    </NuxtLayout>
</template>
<script setup>
import { formatDate } from "~/utils/formatData"
import {useSurveyStore} from "~/stores/survey.js";
/**
 * All `/api/**` are proxies pointing to the local or production server of the backend.
 */
const surveyStore = useSurveyStore()
const { data: surveys } = await surveyStore.getSurveys()

</script>
<style lang="scss">
.my-card {
    margin: 10px 15px
}

.padding-16 {
    padding: 16px;
}
</style>
