<template>
    <v-container style="padding: 16px">
      <v-radio-group @input="event => updateAnswer(event)">
        <v-radio v-for="(option, index) in optionsRef" :value="index" :label="option">
        </v-radio>
      </v-radio-group>
    </v-container>
  </template>
  
  <script>
  export default {
    name: "AnswerTypeSelect",
  }
  </script>
  
  <script setup>
  const emit = defineEmits(['updateAnswer'])
  const props = defineProps({
    question_index: Number,
      question: Object,
      answer: Object,
  })
  const optionsRef = ref(ref(props.question.choices).value.split(','))
  function updateAnswer(event) {
    console.log("updating answer:")
    props.answer.text = optionsRef.value[event.target.value].trim() // name of the selected option
    emit('updateAnswer', props.answer, props.question_index)
  }
  </script>
  <style scoped>
  </style>
  