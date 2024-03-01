<template>
    <Wrapper :questionIndex="questionIndex" v-if="question" v-model="question" :question-type="question.question_type">
        <v-text-field type="number" v-if="question" v-model="question.text" label="Give a number"></v-text-field>
    </Wrapper>
</template>

<script setup>
import questionProxy from "./questionProxy"
import Wrapper from "./Wrapper.vue"

const props = defineProps({
    questionIndex: Number,
})

const question = questionProxy(props)

</script>

