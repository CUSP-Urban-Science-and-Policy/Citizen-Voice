<template>
    <v-textarea 
    style="padding-top: 16px" 
    label="Your answer" 
    variant="outlined" 
    :value="props.answer.text" 
    @input="event => updateAnswer(event)" >
    <!-- call event every time user types in the input field  -->
  </v-textarea>
                <!-- :value should be props.answer.text -->
  <!--  @input="onInput"-->
  </template>


  <script>
  export default {
    name: "AnswerTypeText",
  }
  </script>
  
  <script setup>
  const emit = defineEmits(['updateAnswer']) // always sends the event to the parent component
  const props = defineProps({
    question_index: Number,
    question: Object,
    answer: Object
  })
  function updateAnswer(event) {
    props.answer.text = event.target.value // what user types in the input field
    emit('updateAnswer', props.answer, props.question_index) // emits event with props as payload
  }
  // const answer = ref("")
  //
  // function onInput(e) {
  //   answer.value = e.target.value
  // }
  </script>
  <style scoped>
  </style>
  