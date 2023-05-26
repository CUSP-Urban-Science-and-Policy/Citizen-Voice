<template>
  <v-text-field
    @input="event => updateAnswer(event)"
    hide-details
    single-line
    type="number"
  />
</template>
<!--    v-model="props.answer"-->

<script>
export default {
  name: "AnswerTypeInteger"
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
  emit('updateAnswer', props.answer, question_index)
}

</script>

<style scoped>

</style>
