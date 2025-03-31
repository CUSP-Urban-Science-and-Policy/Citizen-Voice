<template>
    <NuxtLayout name="default">
            <v-sheet 
                max-width="900px"
                class="d-flex align-center flex-wrap mx-auto px-5">
                <div>
                    <h1 class="text-h1 ">Citizen Mapping Tool</h1>
                </div>
                <div class="text-justify py-5">
                    <p class="text-body-1">
                        The <strong>Citizen Mapping Tool</strong> is an <strong>open source tool</strong> that enable researchers and practitioners to create surveys that include 
                        geospatial questions. Those questions are used to collect information about places citizens
                        are familiar with, or to ask them to select locations on a map.
                    </p>
                    <p class="text-body-1 py-2">
                        The tool is designed to be easy to use and accessible to a wide range of users, including those with 
                        limited technical expertise. It is also designed to be flexible and customizable, allowing users to 
                        tailor the survey to their specific needs.
                    </p>
                    <p class="text-body-1 py-2">
                        The demos below showcase some of the cases where the tool can be used.
                    </p>

                </div>
                <div class="row q-col-gutter-sm">
                    <v-card 
                        v-for="survey in surveys"  
                        :title="survey.name"
                        :subtitle="'Published: ' + formatDate(survey.publishe_date)"
                        variant="elevated"
                        max-width="400"
                        class="civo-card"
                        hover
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

const surveyStore = useSurveyStore();
surveyStore.$reset(); // reset SelectedSurvey to null

// const surveys = {};
const {data: surveys} = await surveyStore.getSurveys();
console.log(surveys);

// sets id on surveyStore and redirects to survey/id page
async function selectSurvey (id) {
    surveyStore.selectSurvey(id);
    await navigateTo(`/survey/${id}`);
};

</script>
<style lang="scss">
.civo-card {
    margin: 20px 15px
}

.padding-16 {
    padding: 16px;
}
</style>
