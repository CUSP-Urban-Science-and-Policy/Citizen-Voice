from django.shortcuts import render
from .models import Answer, Question, Survey, Response, PointLocation, PolygonLocation, LineStringLocation, MapView
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import AnswerSerializer, PointLocationSerializer, PolygonLocationSerializer, \
    LineStringLocationSerializer, QuestionSerializer, SurveySerializer, ResponseSerializer, UserSerializer, \
    MapViewSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from datetime import datetime


class AnswerViewSet(viewsets.ModelViewSet):
    """
    Answer ViewSet used internally to query data from database.
    """
    serializer_class = AnswerSerializer

    def get_queryset(response):
        """
        Returns a set of all Answer instances in the database.

        Return:
            queryset: containing all Answer instances
        """

        queryset = Answer.objects.all()
        return queryset

    @staticmethod
    def GetAnswerByQuestion(question_id):
        """
        Get all answers by filtering based either on their related Question.

        Parameters:
            question_id (int): Question ID to be used for finding related Answers

        Return: 
            queryset: containing all Answer instances with this question_id
        """
        queryset = Answer.objects.filter(question=question_id)
        return queryset

    @staticmethod
    def GetAnswerByResponse(response_id):
        """
        Get all answers by filtering based either on their related Response.

        Parameters:
            response_id (int): Response ID to be used for finding related Answers

        Return: 
            queryset: containing all Answer instances with this response_id
        """
        queryset = Answer.objects.filter(response=response_id)
        return queryset


class QuestionViewSet(viewsets.ModelViewSet):
    """
    Question ViewSet used internally to query data from database.

    """

    serializer_class = QuestionSerializer

    def get_queryset(response):
        """
        Returns a set of all Question instances in the database.

        Return:
            queryset: containing all Question instances
        """

        queryset = Question.objects.all()
        return queryset

    @staticmethod
    def GetQuestionByID(id):
        """
        Get a specific Question based on its ID.

        Parameters:
            id (int): Question ID to be used for finding this Question.

        Return: 
            queryset: containing the Question instance with this id
        """

        queryset = Question.objects.filter(id=id)
        return queryset

    @staticmethod
    def GetQuestionBySurvey(survey_id):
        """
        Get specific Questions based on its survey_id.

        Parameters:
            survey_id (int): Survey ID to be used for finding related Questions.

        Return: 
            queryset: containing the Question instance related to this survey
        """

        queryset = Question.objects.filter(survey=survey_id)
        return queryset

    @staticmethod
    def GetOrderedQuestionBySurvey(survey_id, question_order):
        """
        Get specific Questions based on its survey_id, and a specific order.

        Parameters:
            survey_id (int): Survey ID to be used for finding related Questions.
            question_order (int): The order in which the questions in the Survey are to be displayed.

        Return: 
            queryset: containing the Question instance related to this survey, of a given order
        """
        queryset = Question.objects.filter(
            survey=survey_id, order=question_order)
        return queryset


class SurveyViewSet(viewsets.ModelViewSet):
    """
    Survey ViewSet used internally to query data from database.

    """
    # permission_classes = [IsAuthenticated]
    serializer_class = SurveySerializer

    def get_queryset(response):
        """
        Returns a set of all Survey instances in the database.

        Return:
            queryset: containing all Survey instances
        """

        queryset = Survey.objects.all().order_by('name')
        return queryset

    @staticmethod
    def GetSurveyByID(id):
        """
        Get a specific Survey based on its ID.

        Parameters:
            id (int): Survey ID to be used for finding this Survey.

        Return: 
            queryset: containing the Survey instance with this id
        """
        queryset = Survey.objects.filter(id=id)
        return queryset

    @staticmethod
    def GetSurveyByDesigner(designer, unexpired_only=False):
        """
        Get a specific Survey based on its author.

        Parameters:
            designer (int): User ID to be used for finding related Surveys.
            unexpired_only (bool):  True - only unexpired surveys (by current date and time) will be returned
                                    False - all surveys will be returned
                                    default = True

        Return: 
            queryset: containing the Survey instances related to this user
        """
        if unexpired_only:
            now = datetime.now()
            queryset = Survey.objects.filter(
                designer=designer, expire_date__gte=now)
        else:
            queryset = Survey.objects.filter(designer=designer)
        return queryset

    @staticmethod
    def GetSurveyByAvailable():
        """
        Get a all Surveys that are still available (current date is not past expiration date).

        Return: 
            queryset: containing the Survey instances that have not expired yet
        """

        now = datetime.now()
        queryset = Survey.objects.filter(expire_date__gte=now)
        return queryset


class ResponseViewSet(viewsets.ModelViewSet):
    """
    Response ViewSet used internally to query data from database.
    """

    serializer_class = ResponseSerializer

    def get_queryset(response):
        """
        Returns a set of all Response instances in the database.

        Return:
            queryset: containing all Response instances
        """

        queryset = Response.objects.all().order_by('created')
        return queryset

    @staticmethod
    def GetResponseByID(id):
        """
        Get a specific Response based on its ID.

        Parameters:
            id (int): Response ID to be used for finding this Response.

        Return:
            queryset: containing the Response instance with this id
        """
        queryset = Response.objects.filter(id=id)
        return queryset

    @staticmethod
    def GetResponseBySurvey(survey_id):
        """
        Get a specific Response based on its survey.

        Parameters:
            survey_id (int): Survey ID to be used for finding related Responses.

        Return: 
            queryset: containing the Response instances related to this Survey
        """

        queryset = Response.objects.filter(response=survey_id)
        return queryset

    @staticmethod
    def GetResponseByRespondent(respondent):
        """
        Get a specific Response based on its respondent.

        Parameters:
            respondent (int): User ID to be used for finding related Responses.

        Return: 
            queryset: containing the Response instances related to this respondent/ user
        """

        queryset = Response.objects.filter(user=respondent)
        return queryset


class UserViewSet(viewsets.ModelViewSet):
    """
    User ViewSet used internally to query data from database for all users.
    """

    serializer_class = UserSerializer

    def get_queryset(response):
        """
        Returns a set of all User instances in the database.

        Return:
            queryset: containing all User instances
        """

        queryset = User.objects.all().order_by('username')
        return queryset


class PointLocationViewSet(viewsets.ModelViewSet):
    """
    PointLocation ViewSet used internally to query data from database for all users.
    """

    serializer_class = PointLocationSerializer

    def get_queryset(response):
        """
        Returns a set of all PointLocation instances in the database.

        Return:
            queryset: containing all PointLocation instances
        """

        queryset = PointLocation.objects.all()
        return queryset

    @staticmethod
    def GetLocationsByQuestion(question):
        """
        Get a list of Point Locations associated to this question.

        Parameters:
            question (int): Question ID to be used for finding related PointLocations.

        Return: 
            queryset: containing the PointLocations instances related to this Question
        """

        queryset = PointLocation.objects.filter(question=question)
        return queryset

    @staticmethod
    def GetLocationsByAnswer(answer):
        """
        Get a list of Point Locations associated to this answer.

        Parameters:
            answer (int): Answer ID to be used for finding related PointLocations.

        Return: 
            queryset: containing the PointLocations instances related to this Answer
        """

        queryset = PointLocation.objects.filter(answer=answer)
        return queryset


class PolygonLocationViewSet(viewsets.ModelViewSet):
    """
    PolygonLocation ViewSet used internally to query data from database for all users.
    """

    serializer_class = PolygonLocationSerializer

    def get_queryset(response):
        """
        Returns a set of all PolygonLocation instances in the database.

        Return:
            queryset: containing all PolygonLocation instances
        """

        queryset = PolygonLocation.objects.all()
        return queryset

    @staticmethod
    def GetLocationsByQuestion(question):
        """
        Get a list of PolygonLocations associated to this question.

        Parameters:
            question (int): Question ID to be used for finding related PolygonLocations.

        Return: 
            queryset: containing the PolygonLocation instances related to this Question
        """

        queryset = PolygonLocation.objects.filter(question=question)
        return queryset

    @staticmethod
    def GetLocationsByAnswer(answer):
        """
        Get a list of PolygonLocations associated to this answer.

        Parameters:
            answer (int): Answer ID to be used for finding related PolygonLocations.

        Return: 
            queryset: containing the PolygonLocation instances related to this Answer
        """

        queryset = PolygonLocation.objects.filter(answer=answer)
        return queryset


class LineStringLocationViewSet(viewsets.ModelViewSet):
    """
    LineStringLocation ViewSet used internally to query data from database for all users.
    """

    serializer_class = LineStringLocationSerializer

    def get_queryset(response):
        """
        Returns a set of all LineStringLocation instances in the database.

        Return:
            queryset: containing all LineStringLocation instances
        """

        queryset = LineStringLocation.objects.all()
        return queryset

    @staticmethod
    def GetLocationsByQuestion(question):
        """
        Get a list of LineStringLocations associated to this question.

        Parameters:
            question (int): Question ID to be used for finding related LineStringLocations.

        Return: 
            queryset: containing the LineStringLocation instances related to this Question
        """

        queryset = LineStringLocation.objects.filter(question=question)
        return queryset

    @staticmethod
    def GetLocationsByAnswer(answer):
        """
        Get a list of LineStringLocations associated to this answer.

        Parameters:
            answer (int): Answer ID to be used for finding related LineStringLocations.

        Return: 
            queryset: containing the LineStringLocation instances related to this Answer
        """

        queryset = LineStringLocation.objects.filter(answer=answer)
        return queryset


class MapViewViewSet(viewsets.ModelViewSet):
    """
    Question ViewSet used internally to query data from database.

    """

    serializer_class = MapViewSerializer

    def get_queryset(response):
        """
        Returns a set of all MapView instances in the database.

        Return:
            queryset: containing all MapView instances
        """

        queryset = MapView.objects.all()
        return queryset
