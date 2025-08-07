<template>
    <div class="d-flex flex-column">
      <div style="height: 40vh">
      </div>
      <div class="justify-center">
        <div class="d-flex flex-row mb-6 justify-end">
          <v-layout class="justify-center">
            <v-card-actions>
              <v-btn class="" @click="event =>returnToSurvey(event)" color="primary">
                <v-icon dark left>mdi-arrow-left</v-icon>
                <i class="fa-solid fa-arrow-right"></i>
                <span class="q-pa-sm">Return to Survey</span>
              </v-btn>
            </v-card-actions>
            <v-card-actions>
              <v-btn class="" @click="event => finishSurvey(event)" color="primary">
                <i class="fa-solid fa-arrow-left"></i>
                <span class="q-pa-sm">End Survey</span>
                <v-icon dark left>mdi-arrow-right</v-icon>
              </v-btn>
            </v-card-actions>
          </v-layout>
        </div>
      </div>
    </div>
  
  <!--  <v-btn color="primary" @click="event => finishSurvey(event)">-->
  <!--    <i class="fa-solid fa-arrow-right"></i>-->
  <!--    <span class="q-pa-sm">End Survey</span>-->
  <!--  </v-btn>-->
  <!--  <v-btn color="primary" @click="event =>returnToSurvey(event)">-->
  <!--    <i class="fa-solid fa-arrow-right"></i>-->
  <!--    <span class="q-pa-sm">Return to Survey</span>-->
  <!--  </v-btn>-->
  </template>
  
  <script>
  export default {
    name: "endSurvey"
  }
  </script>
  
  <script setup>
  const emit = defineEmits(['returnToSurvey', 'finishSurvey'])
  const props = defineProps({
  })
  function returnToSurvey(event) {
    console.log("endSurvey returnToSurvey")
    emit('returnToSurvey', props)
  }
  function finishSurvey(event) {
    console.log(" endSurvey end survey")
    emit('finishSurvey', props)
  }
  </script>
  <style scoped>
  </style>
  