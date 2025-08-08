<template>
    <v-textarea 
    rows="1" 
    style="padding-top: 16px" 
    label="Your answer" 
    variant="outlined" 
    :value="props.answer.text" 
    @input="event => updateAnswer(event)">
    </v-textarea>
                <!-- :value should be props.answer.text -->
  <!--  @input="onInput"-->
  </template>
  
  <script>
  export default {
    name: "AnswerTypeShortText",
  }
  </script>
  
  <script setup>
  const emit = defineEmits(['updateAnswer'])
  const props = defineProps({
    question_index: Number,
    question: Object,
    answer: Object
  })
  function updateAnswer(event) {
    props.answer.text = event.target.value
    emit('updateAnswer', props.answer, props.question_index)
  }
  // const answer = ref("")
  //
  // function onInput(e) {
  //   answer.value = e.target.value
  // }
  </script>
  <style scoped>
  </style>
  