from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from apiapp.views import SurveyViewSet, QuestionViewSet
from django.contrib.auth.models import User
# from .models import Question, Survey
from django.template.loader import render_to_string
from django.utils.timezone import now
from apiapp.serializers import SurveySerializer
from apiapp.models import Survey

from .forms import SurveyCreationForm


def index(request):
    form = UserCreationForm()
    context = {
        'surveys': SurveyViewSet.GetSurveyByDesigner(request.user.id, unexpired_only=False)
    }
    #TODO: Get all available surveys, do not filter by designer
    return render(request, 'survey_design/index.html', context)


@login_required
def survey(request):
    context = {
        'title': 'Survey Design',
        'surveys': SurveyViewSet.GetSurveyByDesigner(request.user.id, unexpired_only=False)
    }
    return render(request, 'survey_design/survey.html', context)


@login_required
def survey_create(request):
    if request.method == 'POST':
        form = SurveyCreationForm(request.POST)
        if form.is_valid():
            # TODO: override form.is_valid to autofill gaps
            survey_obj = form.save(commit=False)
            survey_obj.display_method = 1
            survey_obj.publish_date = now()
            survey_obj.expire_date = now()
            survey_obj.designer = request.user
            survey_obj.save()
    else:
        form = SurveyCreationForm()
        pass
    context = {
        'title': 'Survey Design',
        'surveys': SurveyViewSet.GetSurveyByDesigner(request.user.id),
    }

    # TODO: Test code
    data = dict()
    surveys = SurveyViewSet.GetSurveyByDesigner(request.user.id)
    data['form_is_valid'] = True
    data['surveys'] = SurveySerializer(surveys, many=True, context={'request': request}).data
    data['html_form'] = render_to_string('survey_design/submodules/ajax/ajax-sidebar-left-surveys.html', context, request=request)
    return JsonResponse(data)


@login_required
def survey_edit(request, survey_id):
    data = dict()
    context = {}
    if request.method == 'GET':
        if SurveyViewSet.GetSurveyByID(survey_id).exists():        
            data['data_exists'] = True
            selected_survey = SurveyViewSet.GetSurveyByID(survey_id)[0]
            context['survey'] = selected_survey
            print(selected_survey, " Yes")
        else:
            data['data_exists'] = False
    data['html_form'] = render_to_string('survey_design/submodules/ajax/map-sidebar-ajax.html', context, request=request)
    return JsonResponse(data)


@login_required
def survey_update(request, survey_id):
    survey = Survey.objects.get(id=survey_id)
    form = SurveyCreationForm(request.POST, instance=survey)
    
    if request.method == 'POST':
        if form.is_valid():
            # TODO: override form.is_valid to autofill gaps
            survey_obj = form.save(commit=False)
            survey_obj.designer = request.user
            survey_obj.save()
    else:
        form = SurveyCreationForm(instance=survey)

    surveys = SurveyViewSet.GetSurveyByDesigner(request.user.id)
    context = {
        'title': 'Survey Design',
        'surveys': surveys,
    }        
    data = dict()
    data['form_is_valid'] = True
    data['surveys'] = SurveySerializer(surveys, many=True, context={'request': request}).data
    data['html_form'] = render_to_string('survey_design/submodules/ajax/ajax-sidebar-left-surveys.html', context, request=request)
    return JsonResponse(data)

@login_required
def survey_delete(request, survey_id):
    survey = Survey.objects.get(id=survey_id)
    
    if request.method == 'POST':
        survey.delete()

    surveys = SurveyViewSet.GetSurveyByDesigner(request.user.id)
    context = {
        'title': 'Survey Design',
        'surveys': surveys,
    }        
    data = dict()
    data['form_is_valid'] = True
    data['surveys'] = SurveySerializer(surveys, many=True, context={'request': request}).data
    data['html_form'] = render_to_string('survey_design/submodules/ajax/ajax-sidebar-left-surveys.html', context, request=request)
    return JsonResponse(data)