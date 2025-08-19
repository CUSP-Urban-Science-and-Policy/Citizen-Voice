import { useQuestionDesignStore } from "~/stores/questionDesign"

const questionStore = useQuestionDesignStore()


/**
 * This set a proxy for the q
 * @param {*} props 
 * @returns Question
 * 
 */
const questionProxy = (props) => {
    return computed({
        get: () => questionStore.currentQuestions[props.questionIndex],
        set: (value) => {
            const question = questionStore.currentQuestions[props.questionIndex]
            const updatedKeys = Object.keys(value).reduce((keys, key) => {
                if (value[key] !== question[key]) {
                    keys.push(key)
                }
                return keys
            }, [])

            if (updatedKeys.length > 0) {
                const updatedQuestion = { ...question, ...value }
                questionStore.setCurrentQuestionValue(props.questionIndex, updatedQuestion)
            }
        }
    })
}



export default questionProxy