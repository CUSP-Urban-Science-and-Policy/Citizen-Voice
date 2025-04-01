from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response as rf_response
from django.middleware import csrf
from .serializers import  PointFeatureSerializer, \
    LineFeatureSerializer, PolygonFeatureSerializer, \
    DashboardAnswerSerializer, DashboardTopicSerializer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from apiapp.models import Answer, PointFeature, \
    PolygonFeature, LineFeature, DashboardTopic

@api_view(['GET'])
def get_csrf_token(request):
    token = csrf.get_token(request)
    return rf_response({'csrf_token': token})

# TODO: consider if using viewset is a good option for this. Viewsets are a fast way to create a CRUD API, 
# but they obfuscate the code; we might want to have more control over the API.
# REF: https://www.django-rest-framework.org/api-guide/viewsets/


# Custom Pagination for this API
class AnswersPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10000


class PointFeatureViewSet(viewsets.ModelViewSet):
    """
    PointLocation ViewSet used internally to query data from database for all users.
    """

    serializer_class = PointFeatureSerializer

    def get_queryset(response):
        """
        Returns a set of all PointFeature instances in the database.

        Return:
            queryset: containing all PointFeature instances
        """

        queryset = PointFeature.objects.all()
        return queryset    


class PolygonFeatureViewSet(viewsets.ModelViewSet):
    """
    PolygonFeature ViewSet used internally to query data from database for all users.
    """

    serializer_class = PolygonFeatureSerializer

    def get_queryset(response):
        """
        Returns a set of all PolygonFeature instances in the database.

        Return:
            queryset: containing all PolygonFeature instances
        """

        queryset = PolygonFeature.objects.all()
        return queryset
    
    @staticmethod
    def GetLocationsByQuestion(question):
        """
        Get a list of PointFeatures associated to this question.

        Parameters:
            question (int): Question ID to be used for finding related PointFeatures.

        Return: 
            queryset: containing the PointFeature instances related to this Question
        """

        queryset = PointFeature.objects.filter(question=question)
        return queryset


    @staticmethod
    def GetLocationsByAnswer(answer):
        """
        Get a list of PolygonFeatures associated to this answer.

        Parameters:
            answer (int): Answer ID to be used for finding related PolygonFeatures.

        Return: 
            queryset: containing the PolygonFeature instances related to this Answer
        """

        queryset = PolygonFeature.objects.filter(answer=answer)
        return queryset


class LineFeatureViewSet(viewsets.ModelViewSet):
    """
    LineStringLocation ViewSet used internally to query data from database for all users.
    """

    serializer_class = LineFeatureSerializer

    def get_queryset(response):
        """
        Returns a set of all LineStringLocation instances in the database.

        Return:
            queryset: containing all LineStringLocation instances
        """

        queryset = LineFeature.objects.all()
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

        queryset = LineFeature.objects.filter(question=question)
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

        queryset = LineFeature.objects.filter(answer=answer)
        return queryset


class DashboardTopicViewSet(viewsets.ModelViewSet):
    """
    A ViewSet that returns the topics associated to a question
    """
    
    serializer_class = DashboardTopicSerializer
    
    def get_queryset(self):
        queryset = DashboardTopic.objects.all()
        return queryset


class AnswerGeoJsonViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A ViewSet that returns GeoJSON data for the answers.
    """
    # Figure out the permissions for the answers, do designers to to see them?
    # permission_classes = [IsAuthenticatedAndSelfOrMakeReadOnly]
    serializer_class = DashboardAnswerSerializer
    pagination_class = AnswersPagination

    def get_queryset(self):
        """
        Returns a set of all Answer instances in the database, or
        filters the queryset based on the query parameters.

        Parameters:
            question (int): Question ID to be used for finding related Answers
            survey (int): Survey ID to be used for finding related Answers

        Returns:
            queryset: 
        """

        # FORWARD FOERIGN KEY: use select_related
        # BACKWARD FOREIGN KEY: use prefetch_related

        queryset = Answer.objects.select_related('mapview__location').exclude(mapview=None).order_by('id')

        # Filter by question Id
        question_id = self.request.query_params.get('question', None)
        if question_id is not None:
            queryset = queryset.filter(question_id=question_id)

        # Filter by survey Id
        survey_id = self.request.query_params.get('survey', None)
        if survey_id is not None:
            queryset = queryset.filter(question__survey_id=survey_id)

        # serializer = DashboardAnswerSerializer(queryset, many=True)
        return queryset

