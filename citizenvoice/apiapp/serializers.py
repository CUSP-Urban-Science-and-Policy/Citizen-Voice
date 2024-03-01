from rest_framework import serializers
from .models import Answer, Question, Survey,PointLocation, PolygonLocation, LineStringLocation, MapView
from .models import Response as ResponseModel
from django.contrib.auth.models import User

# =============================================
# Create serializer classes that allow for exposing certain model fields to be used in the API
# =============================================


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serialises 'response', 'question', 'created', 'updated', 'body'
    fields of the Answer model for the API.
    """
    class Meta:
        model = Answer
        fields = ('response', 'question', 'created', 'updated', 'body')


class QuestionSerializer(serializers.ModelSerializer):
    """
    Serializes 'text', 'order', 'required', 'question_type', 'choices', 'is_geospatial', 'map_view'
    fields of the Question model for the API.
    """
    survey = serializers.PrimaryKeyRelatedField(queryset=Survey.objects.all())

    class Meta:
        model = Question
        fields = ('id', 'text', 'order', 'required', 'question_type',
                  'choices', 'survey', 'is_geospatial', 'map_view')
        read_only_fields = ('id',)

    def create(self, validated_data):
        question = Question.objects.create(
            text=validated_data['text'],
            order=validated_data['order'],
            required=validated_data['required'],
            question_type=validated_data['question_type'],
            choices=validated_data.get('choices', None),
            survey=validated_data['survey'],
            is_geospatial=validated_data.get('is_geospatial', False),
            map_view=validated_data.get('map_view', None),
        )
        return question


class ResponseSerializer(serializers.ModelSerializer):
    """
    Serializes 'created', 'updated', 'survey', 'interview_uuid', 'respondent'
    fields of the Response model for the API.
    """
    survey = serializers.PrimaryKeyRelatedField(queryset=Survey.objects.all())
    respondent = serializers.SerializerMethodField()

    def get_respondent(self, User):
        return UserSerializer(User.respondent).data

    class Meta:
        model = ResponseModel
        fields = ('created', 'updated', 'survey',
                  'respondent', 'interview_uuid')

# TODO: change this to use serializers.ModelSerializer (PrimaryKeyRelatedField)


class SurveySerializer(serializers.HyperlinkedModelSerializer):
    """
    Serialises 'id', 'name', 'description', 'is_published', 'need_logged_user',
    'editable_answers', 'publish_date', 'expire_date', 'public_url', 'designer'
    fields of the Survey model for the API.
    """
    class Meta:
        model = Survey
        fields = ('id', 'name', 'description', 'is_published', 'need_logged_user', 'editable_answers',
                  'publish_date', 'expire_date', 'public_url', 'designer')

# TODO: change this to use serializers.ModelSerializer (PrimaryKeyRelatedField)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serialises 'id', 'username', 'first_name', 'last_name', 'email'
    fields of the User model for the API.
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')

# TODO: change this to use serializers.ModelSerializer (PrimaryKeyRelatedField)


class PointLocationSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serialises 'location', 'name', 'question', 'answer' fields of the PointLocation model for the API.
    """
    class Meta:
        model = PointLocation
        fields = ('location', 'name', 'question', 'answer')

# TODO: change this to use serializers.ModelSerializer (PrimaryKeyRelatedField)


class PolygonLocationSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serialises 'location', 'name', 'question', 'answer' fields of the PolygonLocation model for the API.
    """
    class Meta:
        model = PolygonLocation
        fields = ('location', 'name', 'question', 'answer')

# TODO: change this to use serializers.ModelSerializer (PrimaryKeyRelatedField)


class LineStringLocationSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serialises 'location', 'name', 'question', 'answer' fields of the LineStringLocation model for the API.
    """
    class Meta:
        model = LineStringLocation
        fields = ('location', 'name', 'question', 'answer')


class MapViewSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serialises 'name', 'map_service_url' and 'options'
    fields of the MapView model for the API.
    """
    class Meta:
        model = MapView
        fields = ('id', 'name', 'map_service_url', 'options', 'geometries')
