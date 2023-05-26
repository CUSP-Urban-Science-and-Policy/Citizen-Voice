<template>
  <v-container style="padding: 16px">
    <v-radio-group @input="event => updateAnswer(event)">
      <v-radio v-for="(option, index) in choicesRef" :value="index" :label="option">
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

const choicesRef = ref(ref(props.question.choices).value.split(','))

function updateAnswer(event) {
  console.log("updating answer")
  props.answer.text = event.target.value
  emit('updateAnswer', props.answer, question_index)
}
</script>

<style scoped>

</style>
