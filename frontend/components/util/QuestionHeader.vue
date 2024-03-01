
<template>
    <h4>Question {{question_index + 1}}</h4>
    <h2>{{question.text}}</h2>
  </template>
  
  <script>
  export default {
    name: "QuestionHeader"
  }
  </script>
  
  <script setup>
  const props = defineProps({
    question_index: Number,
    question: Object,
  })
  </script>
  
  <style scoped>
  </style>