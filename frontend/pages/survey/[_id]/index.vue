<template>
    <NuxtLayout name="default">
        <q-page>
            <div class="padding-16">
                <h2>{{ survey.name }}</h2>

                <!-- <p>Counter: {{this.$store.state.counter}}</p>-->
                <p>{{ survey.description }} </p>
                <p>Publish date: {{ formatDate(survey.publish_date) }}</p>
                <p>Expire date: {{ formatDate(survey.expire_date) }}</p>

                <q-btn :to="`/survey/${survey.id}/1`" color="primary">
                    <i class="fa-solid fa-play"></i>
                    <span class="q-pa-sm">Start survey</span>
                </q-btn>

                <!--{{ $route.params.id }}
            <pre>{{ survey }}</pre>-->
            </div>
        </q-page>
    </NuxtLayout>
</template>


<script setup>

</script>

<script setup>
  import { ref } from "vue"
  /**
   * All `/api/**` are proxies pointing to the local or production server of the backend.
   */
  const url = "/api/surveys/"
  const data = ref([])
  const route = useRoute()

  const { data: survey } = await useAsyncData(() => $cmsApi(url + route.params._id));


</script>

