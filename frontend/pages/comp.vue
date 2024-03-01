<template>
    <NuxtLayout name="default" class="pt">
        <div>
    <!-- Other elements of your web page -->
            <p>Answer: {{ yourAnswerObject.text }}</p>
    <AnswerTypeText 
      :question_index="0" 
      :question="yourQuestionObject" 
      :answer="yourAnswerObject" 
      @updateAnswer="handleUpdateAnswer"
    />

    <!-- Other elements of your web page -->
    <AnswerMapView />
  </div>
</NuxtLayout>
</template>

<script>

import AnswerTypeText from '~/components/respondent_view_question_types/AnswerTypeText.vue';

export default {
  components: {
    AnswerTypeText
  },
  data() {
    return {
      yourQuestionObject: {
        text: 'What is your favorite color?',
        survey: 1,
        id: 1,
      }, // Replace with your actual question object
      yourAnswerObject: { text: '' }, // Replace with your actual answer object
    };
  },
  methods: {
    handleUpdateAnswer(updatedAnswer, questionIndex) {
      // Handle the updated answer here
      console.log(updatedAnswer, questionIndex);
    },
  },
};
</script>