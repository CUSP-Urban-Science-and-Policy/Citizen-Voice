export default class Answer {
    /**
     *
     * @param sId Integer indicating the survey
     * @param rId Integer indicating the response
     * @param qIndex
     */
    constructor(sId, rId, qIndex) {
      this.surveyId = sId;
      this.responseId = rId;
      this.questionIndex = qIndex;
      // this.created = new Date()
      this.text = "";
    }
  
  
    get surveyId() {
      return this._surveyId
    }
  
    get responseId() {
      return this._responseId
    }
  
    get text() {
      return this._text
    }
  
    get questionIndex() {
      return this._questionIndex
    }
  
    set surveyId(id) {
      this._surveyId = id;
    }
  
    set responseId(id) {
      this._responseId = id;
    }
  
    set text(answer) {
      this._text = answer;
    }
  
    set questionIndex(id) {
      this._questionIndex = id;
    }
  
  }