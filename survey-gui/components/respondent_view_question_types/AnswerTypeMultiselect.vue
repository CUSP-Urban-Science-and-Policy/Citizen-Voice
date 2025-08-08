<template>
    <v-container fluid @input="event => updateAnswer(event)">
      <v-checkbox v-for="(choice, index) in choicesRef"
        v-model="selected"
        :label="choice"
        :value="index"
      ></v-checkbox>
    </v-container>
  </template>
  
  <script>
  export default {
    name: "AnswerTypeSelectMultiple",
  }
  </script>
  
  <script setup>
  const emit = defineEmits(['updateAnswer'])
  const answers = ref([])
  const selected = ref([])
  const props = defineProps({
    question_index: Number,
    question: Object,
    answer: Object,
  })

  const choicesRef = ref(ref(props.question.choices).value.split(','))
  function updateAnswer(event) {
    console.log("selected  answer:", event.target.value)
    props.answer.text =  selected.value.map(item => choicesRef.value[item]).join().trim() // should be a comma separated string of all selected options
    emit('updateAnswer', props.answer, props.question_index)
  }
  </script>
  <style scoped>
  </style>
  