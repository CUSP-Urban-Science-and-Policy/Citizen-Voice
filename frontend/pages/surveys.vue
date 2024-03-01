<template>
    <NuxtLayout name="default">
        <v-sheet class="d-flex mx-auto px-4">
            <h1 class="h2 mb-4">Surveys</h1>
            <div class="row q-col-gutter-sm">
                <v-card 
                    v-for="survey in surveys"  
                    :title="survey.name"
                    :subtitle="'Published: ' + formatDate(survey.publishe_date)"
                    variant="elevated"
                    width="400"
                    class="my-card"
                    >
                 
                        <v-card-actions>
                            <v-btn @click="selectSurvey(survey.id)" color="primary" variant="elevated">
                            Participate
                            </v-btn>
                        </v-card-actions>
                        <v-divider></v-divider>
                </v-card>
            </div>
        </v-sheet>
    </NuxtLayout>
</template>
<script setup>
import { formatDate } from "~/utils/formatData"

// TODO [MANUEL]: useSubmitForm is not  in survey.js
// import { useSubmitForm } from "~/stores/survey.js";



/**
 * All `/api/**` are proxies pointing to the local or production server of the backend.
 */
// const url = "/api/surveys/"
// const { data: surveys } = await useAsyncData(() => $cmsApi(url));
const surveyStore = useSurveyStore();
surveyStore.$reset(); // reset SelectedSurvey to null

const {data: surveys} = await surveyStore.getSurveys();

// sets id on surveyStore and redirects to survey/id page
function selectSurvey (id) {
    surveyStore.selectSurvey(id);
    navigateTo(`/survey/${id}`);
};

</script>
<style lang="scss">
.my-card {
    margin: 20px 15px
}

.padding-16 {
    padding: 16px;
}
</style>
