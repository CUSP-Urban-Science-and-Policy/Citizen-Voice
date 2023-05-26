<template>
  <v-container fluid @input="event => updateAnswer(event)">
<!--    <p>{{ selected }}</p>-->
    <v-checkbox
      v-model="selected"
      label="Option 1"
      value="Option 1"
    ></v-checkbox>
    <v-checkbox
      v-model="selected"
      label="Option 2"
      value="Option 2"
    ></v-checkbox>
  </v-container>
<!--  <h2>{{selected}}</h2>-->
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

function updateAnswer(event) {
  props.answer.text = selected.value
  emit('updateAnswer', props.answer, props.question_index)
}
</script>

<style scoped>

</style>
