import { defineStore } from 'pinia'
import { useUserStore } from './user'
import { useGlobalStore } from './global'
import setRequestConfig from './utils/setRequestConfig';


export const useStoreResponse = defineStore('response', {
    state: () => ({
        response: null,
        currentQuestion: 1,
        answersToCurrentSurvey: [],
    }),
    getters: {
        getAnswersToCurrentSurvey: (state) => state.answersToCurrentSurvey
    },
    actions: {
        setResponse(response) {
            this.response = response
        },
        setCurrentQuestion(questionNumber) {
            this.currentQuestion = questionNumber
        },
        async getResponse({ id }) {
            console.log('get response id //> ', id)
            const { data: survey } = await useAsyncData(() => $cmsApi('/api/surveys/' + id + '/'));
            return survey
        },

        /**
         * Creates a new respondent object linked to a survey and stores the id in the localstorage this way we know if it's the same respondent over multiple questions
         * First it checks if the respondent-id is not already in the localstorage, if so it skips the respondent creation
         * @param {*} param0 
         * @returns 
         * 
         * @question what happens if a respondent does multiple surveys, do we need to link all the surveys?
         */
        async createResponse({ id }) {

            // First let's check if there is not a response id already in the local storage



            const config = setRequestConfig({
                method: 'POST', body: {
                    survey: id
                }
            })

            // const config = {
            //     headers: {
            //         'Content-Type': 'application/json',
            //         // 'X-CSRFToken': csrftoken,
            //     },
            //     // method: 'POST',
            //     // Pass the data for the new Response object as the request body
            //     // TODO: have the respondent set to the logged in user
            //     body: {
            //         // survey: '/api/surveys/' + surveyPK + "/",
            //         survey: surveyPK,
            //         // Pass the data for the new Response object as the request body
            //         // TODO: have the respondent set to the logged in use
            //         // survey: '/api/surveys/' + id + "/",

            //         respondent: "/api/users/me/"
            //     },
            // }

            // First let's see if the respondent id is not already set
            if (localStorage.getItem("respondent-id") !== null) {
                return localStorage.getItem("respondent-id")
            }

            const { data: response, pending, error } = await useAsyncData(() => $cmsApi('/api/responses/create-response/', config));

            if (response?.value?.response_id) {
                localStorage.setItem('respondent-id', response.value.response_id);
                return response.value.response_id
            }

            return null

        },
        async submitAnswer(answers) {
            const user = useUserStore()
            const global = useGlobalStore()
            const csrftoken = user.getCookie('csrftoken');
            const token = user.getAuthToken

            const config = {
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken,
                },
                method: 'POST',
                //   // Pass the data for the new Response object as the request body
                //   // TODO: have the respondent set to the logged in user
                body: {
                    // survey: '/api/surveys/' + id + "/",
                    respondent: "/api/users/me/",
                    answers: answers,
                    responseId: 1,
                },
            }

            if (token) {
                config.headers['Authorization'] = `Token ${token}`
            }

            const { data: survey, pending, error } = await useAsyncData('retrieveResponse', () => $cmsApi('/api/responses/submit-response/', config));
            // console.log("CreateResponse retrieved survey:")
            // console.log(survey)

            console.log("Response:")
            console.log(answers)
        }

    }
})
