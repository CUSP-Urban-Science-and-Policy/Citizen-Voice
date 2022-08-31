from django.shortcuts import render
from .models import Answer, Question, Survey, Response
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import (
    AnswerSerializer,
    QuestionSerializer,
    SurveySerializer,
    ResponseSerializer,
    UserSerializer,
)
from django.contrib.auth.models import User


# Create a ViewSet that queries all the instances of Answer in the database, and parse them through the serializer
class AnswerViewSet(viewsets.ModelViewSet):
    """
    Answer ViewSet used internally to query data from database. The following functions are defined in this viewset:

    GetAnswers() - returns a set of all Answer instances in the database

    GetAnswer(int response_id, int question_id) - returns a filtered list of Answer instances based either on a given response_id
                                            or a given question_id. Only one must be provided. The id that is provided is
                                            used to filter by that particular metric.

    """

    # Get all answers
    @staticmethod
    def GetAnswers():
        queryset = Answer.objects.all()
        serializer_class = AnswerSerializer
        return queryset

    # Get all answers by filtering based either on their related Response or Question
    @staticmethod
    def GetAnswer(response_id=0, question_id=0):
        if response_id == 0:
            queryset = Answer.objects.filter(question=question_id)
            serializer_class = AnswerSerializer
            return queryset
        elif question_id == 0:
            queryset = Answer.objects.filter(response=response_id)
            serializer_class = AnswerSerializer
            return queryset


# Create a ViewSet that queries all the instances of Question in the database, and parse them through the serializer
class QuestionViewSet(viewsets.ModelViewSet):
    """
    Question ViewSet used internally to query data from database. The following functions are defined in this viewset:

    GetQuestions() - returns a set of all Question instances in the database

    GetQuestion(int id, int survey_id) - returns a filtered list of Question instances based either on a given question_id
                                        or a given survey_id. Only one must be provided. The id that is provided is
                                        used to filter by that particular metric.

    """

    # Get all questions
    @staticmethod
    def GetQuestions():
        queryset = Question.objects.all()
        serializer_class = QuestionSerializer
        return queryset

    # Get a specific Question based on its ID
    @staticmethod
    def GetQuestion(id=0, survey_id=0):
        if survey_id == 0:
            queryset = Question.objects.filter(id=id)
            serializer_class = QuestionSerializer
            return queryset
        elif id == 0:
            queryset = Question.objects.filter(survey=survey_id)
            serializer_class = QuestionSerializer
            return queryset

    # Get a Questions based on their survey ID
    @staticmethod
    def GetQuestionsFromSurvey(survey_id):
        queryset = SurveyViewSet.GetSurvey(survey_id)[0].question_set.all()
        serializer_class = QuestionSerializer
        return queryset

    # Get a specific Question based on its survey ID and order in the survey
    @staticmethod
    def GetOrderedQuestionFromSurvey(survey_id, question_order):
        queryset = (
            SurveyViewSet.GetSurvey(survey_id)[0]
            .question_set.all()
            .filter(order=question_order)
        )
        serializer_class = QuestionSerializer
        return queryset


# Create a ViewSet that queries all the instances of Survey in the database, and parse them through the serializer
class SurveyViewSet(viewsets.ModelViewSet):
    """
    Survey ViewSet used internally to query data from database. The following functions are defined in this viewset:

    GetSurveys() - returns a set of all Survey instances in the database

    GetSurvey(int id) - returns an instance of Survey with the ID that was provided in the function.

    """

    # Get all surveys
    @staticmethod
    def GetSurveys():
        queryset = Survey.objects.all().order_by("name")
        serializer_class = SurveySerializer
        return queryset

    # Get a specific Survey based on its ID
    @staticmethod
    def GetSurvey(id):
        queryset = Survey.objects.filter(id=id)
        serializer_class = SurveySerializer
        return queryset


# Create a ViewSet that queries all the instances of Response in the database, and parse them through the serializer
class ResponseViewSet(viewsets.ModelViewSet):
    """
    Response ViewSet used internally to query data from database. The following functions are defined in this viewset:

    GetResponses() - returns a set of all Response instances in the database

    GetResponse(int survey_id, int user_id) - returns a filtered list of Response instances based either on a given survey_id
                                            or a given user_id. Only one must be provided. The id that is provided is
                                            used to filter by that particular metric.

    """

    # Get all responses
    @staticmethod
    def GetResponses():
        queryset = Response.objects.all().order_by("created")
        serializer_class = ResponseSerializer
        return queryset

    # Get all responses by filtering based either on their related Survey or User
    @staticmethod
    def GetResponse(survey_id=0, user_id=0):
        if survey_id == 0:
            queryset = Response.objects.filter(question=user_id)
            serializer_class = ResponseSerializer
            return queryset
        elif user_id == 0:
            queryset = Response.objects.filter(response=survey_id)
            serializer_class = ResponseSerializer
            return queryset


# Create a ViewSet that queries all the instances of User in the database, and parse them through the serializer
class UserViewSet(viewsets.ModelViewSet):
    """
    USer ViewSet used internally to query data from database for all users.
    The following functions are defined in this viewset:
        GetUsers() - returns a set of all User instances in the database
    """

    # Get all users
    @staticmethod
    def GetUsers():
        queryset = User.objects.all().order_by("username")
        serializer_class = UserSerializer
        return queryset
