<template>
  <v-text-field @input="event => updateAnswer(event)" 
    type="date" 
    label="Date"
    clearable
    >
  </v-text-field>
</template>
<!--    v-model="props.answer"-->

<script>
export default {
  name: "AnswerTypeDate",
}
</script>

<script setup>
const emit = defineEmits(['updateAnswer'])
const props = defineProps({
  question_index: Number,
  question: Object,
  answer: Object,
})
function updateAnswer(event) {
  console.log("updating answer")
  props.answer.text = event.target.value
  emit('updateAnswer', props.answer, props.question_index)
}
</script>
<style scoped>
</style>
