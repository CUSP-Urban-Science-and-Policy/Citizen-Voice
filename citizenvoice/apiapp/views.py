from .models import Answer, Question, Survey, Response, PointLocation, PolygonLocation, LineStringLocation, MapView
from django.http import HttpResponse
from .permissions import IsAuthenticatedAndSelfOrMakeReadOnly, IsAuthenticatedAndSelf
from rest_framework.decorators import api_view
from rest_framework.mixins import UpdateModelMixin
from django.middleware import csrf
from django.http import HttpResponse
from django.utils import timezone
from rest_framework import viewsets, status
from .serializers import AnswerSerializer, PointLocationSerializer, PolygonLocationSerializer, \
    LineStringLocationSerializer, QuestionSerializer, SurveySerializer, ResponseSerializer, UserSerializer, \
    MapViewSerializer

from rest_framework.permissions import AllowAny, IsAuthenticated

from django.contrib.auth.models import User
from datetime import datetime
from django.shortcuts import get_object_or_404

from rest_framework.decorators import action
from rest_framework.response import Response as rf_response


@api_view(['GET'])
def get_csrf_token(request):
    token = csrf.get_token(request)
    return rf_response({'csrf_token': token})


class AnswerViewSet(viewsets.ModelViewSet):
    """
    Answer ViewSet used internally to query data from database.
    """
    # Figure out the permissions for the answers, do designers to to see them?
    # permission_classes = [IsAuthenticatedAndSelfOrMakeReadOnly]
    serializer_class = AnswerSerializer

    def get_queryset(self):
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


class QuestionViewSet(viewsets.ModelViewSet, UpdateModelMixin):
    """
    Question ViewSet used to query data from database.
    The `create` method is overwritten to accept one data object or a array of objects.
    """
    permission_classes = [IsAuthenticatedAndSelfOrMakeReadOnly]
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def create(self, request, *args, **kwargs):
        """
        Here we are overwriting the default create method from the Django REST framework to update or create Questions by list or by single instances
        """
        # Checks if the request data is a list, and if not it wraps it in a list
        data = request.data if isinstance(
            request.data, list) else [request.data]
        questions = []
        """
        Here we iterates over each item in the list and checks if it has an 'id' field. If it does, it retrieves the existing Question object with that ID (if it exists). If it doesn't have an 'id' field, it creates a new Question object.
        """
        for question_data in data:
            if 'id' in question_data:
                question = Question.objects.filter(
                    pk=question_data['id']).first()
                if question is None:
                    continue
                serializer = self.get_serializer(
                    question, data=question_data, partial=True, context={'request': request})
            else:
                serializer = self.get_serializer(
                    data=question_data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            question = serializer.save()
            questions.append(question)

        update_fields = ['text', 'order', 'required', 'question_type',
                         'choices', 'survey', 'is_geospatial', 'map_view']

        # update or create multiple questions in bulk
        Question.objects.bulk_update_or_create(questions, update_fields, match_field='id')

        serializer = self.get_serializer(questions, many=True)
        headers = self.get_success_headers(serializer.data)
        return rf_response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        update_fields = ['text', 'order', 'required', 'question_type',
                         'choices', 'survey', 'is_geospatial', 'map_view']
        serializer.save(update_fields=update_fields)

    def perform_update(self, serializer):
        serializer.save(update_fields=['text', 'order', 'required', 'question_type', 'choices', 'survey', 'is_geospatial', 'map_view'], update_conflicts={
                        'text': 'keep',
                        'order': 'keep',
                        'required': 'keep',
                        'question_type': 'keep',
                        'choices': 'keep',
                        'survey': 'keep',
                        'is_geospatial': 'keep',
                        'map_view': 'keep'
                        })

    @action(detail=True, methods=['get'])
    def ordered_questions(self, request, pk=None):
        """
        Retrieve a list of questions for a given survey, ordered by the 'order' field.
        API url: `/api/questions/{survey_id}/ordered_questions`

        Parameters:
            request (Request): The request object used to make the API call.
            pk = survey_id (int): The primary key of the Survey instance to retrieve questions for.

        Returns:
            Response: A JSON response containing a list of serialized Question instances.
        """
        survey = get_object_or_404(Survey, pk=pk)
        questions = survey.question_set.all().order_by('order')
        serializer = self.get_serializer(questions, many=True)
        return rf_response(serializer.data)


class SurveyViewSet(viewsets.ModelViewSet):
    """
    Survey ViewSet used internally to query data from database.

    """
    permission_classes = [IsAuthenticatedAndSelfOrMakeReadOnly]
    serializer_class = SurveySerializer

    def get_queryset(response):
        """
        Returns a set of all Survey instances in the database.

        Return:
            queryset: containing all Survey instances
        """
        queryset = Survey.objects.all().order_by('name')

        return queryset

    @action(detail=False, methods=['GET'], url_path='my-surveys')
    def my_surveys(self, request, *args, **kwargs):
        print("Getting my surveys...")

        user = self.request.user
        print(type(user))
        if (type(user) == User):
            surveys_of_user = Survey.objects.all().filter(designer=user.id).order_by('name')
            survey_serializer = self.get_serializer(surveys_of_user, many=True)
            # print("User Id: ", user.id)
            # print(survey_serializer.data)
            return rf_response(survey_serializer.data)

        return rf_response({})

    @action(detail=False, methods=['POST'], url_path='create-survey')
    def create_survey(self, request, *args, **kwargs):
        print("Creating a new survey...")

        user = self.request.user
        if type(user) is User:
            survey_name = self.request.data["name"]
            survey_description = self.request.data["description"]
            once_up_a_time = datetime.now()

            tz_aware_datetime = timezone.make_aware(once_up_a_time)  # Convert to timezone-aware datetime

            survey = Survey(name=survey_name, description=survey_description,
                            publish_date=tz_aware_datetime, expire_date=tz_aware_datetime, designer=user)
            survey.save()

            survey_serializer = SurveySerializer(survey, context={'request': request})  # Pass the request context
            return rf_response(survey_serializer.data)
        else:
            print("User was anonymous")
        return rf_response(None)

    # TODO: remove this one because we are now directly getting the questions from the QuestionViewSet
    @action(detail=True, methods=['GET'], url_path='questions')
    def get_questions_of_survey(self, request, pk=None):
        print("Retreiving questions of survey...")
        user = self.request.user
        survey = Survey.objects.get(id=pk)
        if (survey.is_published):
#             if type(user) is User:
#                 survey = Survey.objects.get(id=pk)
#                 if (survey.designer != user.id):
#                     print("uses is not the designer")
#                     print(
#                         f"User id: {user.id} \nDesigner id: {survey.designer_id}")
#                     rf_response([])
            questions = Question.objects.all().filter(survey_id=pk).order_by('order')
            question_serializer = QuestionSerializer(
                questions, many=True, context={'request': request})
            print(question_serializer.data)
            return rf_response(question_serializer.data)
#             else:
#                 print("User was anonymous")
        return rf_response([])

    # @action(detail=True, methods=['post'])
    # def CreateSurvey(response):
    #     """
    #     Create a survey
    #     """
    #     data = JSONParser().parse(response)
    #     survey_serializer = SurveySerializer(data=data, context={'request': response})
    #     if survey_serializer.is_valid():
    #         survey_serializer.save()
    #         return JsonResponse(survey_serializer.data, status=status.HTTP_201_CREATED)
    #     return JsonResponse(survey_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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


    @action(detail=False, methods=['Post'], url_path='submit-response')
    def submitResponse(self, request, *args, **kwargs):
        print("submitting Response")

        user = self.request.user
        answers = self.request.data["answers"]
        responseId = self.request.data['responseId']
        questionId = 1 # TODO: get id of question
        print(answers)
        print(responseId)



        if type(user) is User:
            print("User:")
            print(str(User))
        else:
            print("User was anonymous")

        time = datetime.now()
#         resp = Response(id=1, created=time, updated=time, survey=Survey.objects.get(pk=20), interview_uuid='123', respondent=User.objects.get(pk=1))
#         resp.save()

        for answer in answers:
            text = answer['_text']
            print('lalala')
            resp = Response.objects.get(pk=int(responseId))
            quest = Question.objects.get(pk=1)
            storedAnswer = Answer(response=resp, question=quest,
             created=time, updated=time, body=text)
            print(str(answer))
            #answer.save()
        return rf_response(None)

#    @action(detail=True, methods=['GET'], url_path='questions')
#     def get_questions_of_survey(self, request, pk=None):

    @action(detail=False, methods=['GET'], url_path='create-response')
    def createResponse(self, request, *args, **kwargs):
        print("creating Response")
        time = datetime.now()
        survey = Survey.objects.get(pk=1)
        print(survey)

        user = self.request.user
        resp = None
        if type(user) is User:
            resp = Response(created=time, updated=time, survey=survey)
            print(resp)
        else:
            print("User was anonymous")
            resp = Response(created=time, updated=time, survey=survey)
            print(resp)
#             resp.save()

        response_serializer = ResponseSerializer(resp, context={'request': request})
        print(response_serializer.data)
#             return rf_response(question_serializer.data)
#         created = models.DateTimeField(_("Date response was submitted"), auto_now_add=True)
#         updated = models.DateTimeField(_("Last edit"), auto_now=True)
#         survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
#         interview_uuid = models.CharField(_("Unique ID of interview"), max_length=150)
#         respondent = models.ForeignKey(User, on_delete=models.CASCADE)
        return rf_response(response_serializer.data)

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

    permission_classes = [IsAuthenticatedAndSelf]
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

    @action(detail=False, methods=['get'])
    def id_names(self, request):
        mapviews = MapView.objects.values('id', 'name')
        return Response(mapviews)
