import { defineStore } from 'pinia';
import { useUserStore } from './user';
import { useGlobalStore } from './global';
import setRequestConfig from './utils/setRequestConfig';
import { useSurveyStore } from './survey';

export const useStoreResponse = defineStore('response', {
    
    state: () => 
        // required data for the response store
        // responseId // if null it means that the respondent 
        // respondent
        // currentQuestion
        // surveyId
        // answersToCurrentSurvey
       { 
        return { 
            responseData: {},
            answers: 
            [
                // expects and array of objects with the following structure
                // {
                // question_index: integer,
                // body: text,
                // }
            ],
        
        } },
    getters: {
        responseId() {
            return this.responseData.interview_uuid
        },
        // when using ARROW functions, state should be passed as an argument to be able to 
        // access the state of the store using 'this'
        // getAnswersToCurrentSurvey: (state) => this.answersToCurrentSurvey
        
    },
    actions: {
        updateAnswer(answer) {
            // updates an answer in the array of answers
            // answer must have the following structure
            // {
            // question_id: integer,
            // text: text,
            // }
            const existingAnswer = this.answers.find(a => a.question_id === answer.question_id);
            if (existingAnswer) {
                existingAnswer.text = answer.text;
            }
            else {
                this.answers.push(answer);
            }
    
        },

        async createResponse({ surveyId, respondentId=null  }) {
            /**
         * Creates a respondent in the backend and initializes the localstorage with:
         * respondent, iterview-uuid, and message
         * 
         * @param {number} surveyId the survey id
         * @param {number} respondentId the respondent id, null values means that the respondent is not logged in, and the backend will create register the respondent as anonymous (if allowed by the survey)
         * @returns {object} the response object 
         * 
         * @question what happens if a respondent does multiple surveys, do we need to link all the surveys?
         */
            
            // console.log('surveyId //> ', surveyId);
            const user = useUserStore()
            const csrftoken = user.getCookie('csrftoken');
            const token = user.getAuthToken

            const config = setRequestConfig({
                method: 'POST', 
                body: {
                    survey: surveyId,
                    respondent: respondentId  // this is required by the api
                }
            });

            // checks if the interview_uuid is already in the localstorage. If it is, it means that the response has already been created and the localstorage has been initialized   
            // TODO: fix 
            // if ("interview_uuid" in state.data) {
            //     console.log('surveyID in respose store //> ', surveyId);
            //     return localStorage.getItem('respondent-id')
            // }

            if (!("interview_uuid" in this.responseData)) {

                const { data: response, pending, error} = await useAsyncData(() => $cmsApi('api/responses/response/create-response/', config));

                const responseData = await response.value;
                this.responseData = responseData;
                console.log('responseData //> ', responseData);
            }
        },

        getRespondentId(){
            if (localStorage?.getItem('respondent-id') !== null) {
                return localStorage.getItem('respondent-id')
            }
            return null
        },
        setResponse(response) {
            // [manuel]: Change the value of the response. Is response the right name? is response here the answer to a question?
            this.responseId = response
        },
        setCurrentQuestion(questionNumber) {
            this.currentQuestion = questionNumber
        },


        async getSurvey({ id }) {
            
            const { data: survey } = await useAsyncData(() => $cmsApi('/api/surveys/' + id)); 

            if (survey) {
                console.log('survey.value.id in get Survey//> ', survey.value.id);
                this.surveyId = survey.id;
            }

            return survey
        },
        
        clearAnswers() {
            // Clear all the answers
            this.answers = []
        },
        async submitAnswer(response_url, question_url, answer_value) {
            const user = useUserStore();
            const global = useGlobalStore();
            const csrftoken = user.getCookie('csrftoken');
            const token = user.getAuthToken;

            const config = {
                headers : {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken,
                },
                method: 'POST',
                // pas the data for the new Response object as the request body
                
                // TODO: have the repondent set to the logged in user 
                body: {
                    response: response_url,
                    question: question_url,
                    body: answer_value
                }
            };
            if (token) {
                config.headers['Authorization'] = `Token ${token}`
            };

            const {data: response, pending, error} = await useAsyncData('submitAnswer', () => $cmsApi('/api/answers/', config));

            if (response) {
                console.log('response submitted //> ');
            }
        
        }

        // TODO: CONTINUE HERE
        // implement the submit-response endpoint in the backend

            // if (token) {
            //     config.headers['Authorization'] = `Token ${token}`

            // }

            // const {data: _response}  = await useAsyncData( () => $cmsApi('/api/responses/', config));

            // console.log('response in response store//> ', _response.value.interview_uuid);

            // // return _response
            // this.setResponse(_response.value.interview_uuid)
            // return true
            // // console.log('id //> ', id);
            // // console.log(survey)

        
    }
})