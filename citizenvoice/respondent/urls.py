from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='respondent-index'),
    path('survey', views.survey, name='respondent-home'),
    path('survey/<int:survey_id>/', views.survey_detail, name='respondent-survey-detail'),
    path('survey/<int:survey_id>/question/<int:question_order>/response/<int:response_id>/', views.question_detail,
         name='respondent-question-detail'),
]

