<template>
    <Wrapper :questionIndex="questionIndex" v-if="question" v-model="question" :question-type="question.question_type">
        <v-textarea v-if="question" v-model="question.text" label="Text of the Question" variant="outlined"></v-textarea>
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

