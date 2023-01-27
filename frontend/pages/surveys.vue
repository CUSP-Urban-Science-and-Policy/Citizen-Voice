<template>
    <NuxtLayout name="default">
        <q-page>
            <div class="padding-16">
                <h2>Surveys</h2>
                <div class="row q-col-gutter-sm">
                    <q-card v-for="survey in surveys" style="min-width: 300px;" class="my-card col" flat bordered>
                        <q-card-section horizontal>
                            <q-card-section class="q-pt-xs flex column space-between ">
                                <div class="text-h5 q-mt-sm q-mb-xs">{{
                                    survey.name
                                }}</div>
                                <p class="text-caption ">
                                    {{ survey.description }}
                                </p>
                                <div class=" text-caption">
                                    <span class="">Publish date: {{ formatDate(survey.publish_date) }}</span><br />
                                    <span>Expire date: {{ formatDate(survey.expire_date) }}</span>
                                </div>
                                <q-card-actions style="padding-left: 0" margin="0" class="item-end q-mt-auto">
                                    <q-btn :to="`/survey/${survey.id}`" color="primary">
                                        <i class="fa-solid fa-play"></i>
                                        Start survey
                                    </q-btn>
                                </q-card-actions>
                            </q-card-section>

                            <q-card-section class="col flex flex-center">
                                <q-img class="rounded-borders" src="https://cdn.quasar.dev/img/parallax2.jpg" />
                            </q-card-section>
                        </q-card-section>
                    </q-card>
                </div>
            </div>
        </q-page>
    </NuxtLayout>

</template>
<script setup>
import { formatDate } from "~/utils/formatData"
/**
 * All `/api/**` are proxies pointing to the local or production server of the backend.
 */
const url = "/api/surveys/"
const { data: surveys } = await useAsyncData(() => $cmsApi(url));
</script>
<style lang="scss">
.my-card {
    margin: 10px 15px
}

.padding-16 {
    padding: 16px;
}
</style>
