from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="survey-design-index"),
    # ex: /survey/
    path("survey", views.survey, name="survey-list"),
    # ex: /survey/1/
    path("survey/<int:survey_id>/", views.survey_detail, name="survey-detail"),
    # ex: /survey/1/question/1
    path(
        "survey/<int:survey_id>/question/<int:question_order>/",
        views.question_detail,
        name="question-detail",
    ),
]
