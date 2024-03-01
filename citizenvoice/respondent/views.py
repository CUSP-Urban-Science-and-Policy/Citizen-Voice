from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from apiapp.views import SurveyViewSet, QuestionViewSet, ResponseViewSet, PointLocationViewSet
from .forms import ResponseCreationForm, AnswerCreationForm
from django.utils import timezone

# Create your views here.


def index(request):
    context = {
        'surveys': SurveyViewSet.GetSurveyByAvailable()
    }
    #TODO: Get all available surveys, do not filter by designer
    return render(request, 'respondent/index.html', context)


def survey(request):
    context = {
        'title': 'Survey Design',
        'surveys': SurveyViewSet.GetSurveyByDesigner(request.user.id, unexpired_only=True)
    }
    return render(request, 'respondent/index.html', context)

def survey_detail(request, survey_id):
    form = ResponseCreationForm()

    if request.method == 'POST':
        form = ResponseCreationForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.created = timezone.now()
            obj.updated = timezone.now()
            obj.survey = SurveyViewSet.GetSurveyByID(survey_id)[0]
            #TODO: Discuss whether following fields are optional or not
            obj.interview_uuid = "123"
            obj.respondent = request.user
            obj.save()
        return redirect(question_detail, survey_id, 1, obj.id)

    context = {
        'form': form,
        'survey_id': survey_id
    }
    try:
        context['survey'] = SurveyViewSet.GetSurveyByID(survey_id)[0]
        context['questions_of_survey'] = QuestionViewSet.GetQuestionBySurvey(survey_id)
    except:  # Survey.DoesNotExist
        # pass for now, we might add some warning in the future
        raise e
    return render(request, 'respondent/index.html', context)


def question_detail(request, survey_id, question_order, response_id):
    answer_form = AnswerCreationForm()

    if request.method == 'POST':
        answer_form = AnswerCreationForm(request.POST)
        if answer_form.is_valid():
            obj = answer_form.save(commit=False)
            obj.created = timezone.now()
            obj.updated = timezone.now()
            obj.response = ResponseViewSet.GetResponseByID(response_id)[0]
            obj.question = QuestionViewSet.GetOrderedQuestionBySurvey(survey_id, question_order)[0]
            obj.save()
        if SurveyViewSet.GetSurveyByID(survey_id)[0].question_count() > question_order:
            return redirect(question_detail, survey_id, question_order + 1, response_id)
        else:
            return redirect(index)

    if request.method == 'GET':
        request_data = request.GET
        print(request_data)


    context = {
        'answer_form': answer_form,
        'title': 'Survey Design',
        'surveys': SurveyViewSet.GetSurveyByDesigner(request.user.id),
        'survey_id': survey_id,
        'respondent': True,
        'button_value': "End Survey",
    }
    try:
        context['survey'] = SurveyViewSet.GetSurveyByID(survey_id)[0]
        context['question'] = QuestionViewSet.GetOrderedQuestionBySurvey(survey_id, question_order)[0]
        context['locations_by_question'] = PointLocationViewSet.GetLocationsByQuestion(context['question'])

        if context['survey'].question_count() > question_order:
            context['next_question_order'] = question_order + 1
            context['button_value'] = "Next Question"


    except Exception as e:
        # Survey.DoesNotExist
        # pass for now, we might add some warning in the future
        raise e

    return render(request, 'respondent/index.html', context)

