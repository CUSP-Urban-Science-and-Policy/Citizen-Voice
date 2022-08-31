# ====================================================================================================================
#
# Created with reference "Build a REST API in 30 minutes with Django REST Framework" by Bennett Garner, May 17, 2019
# https://medium.com/swlh/build-your-first-rest-api-with-django-rest-framework-e394e39a482c
#
# ====================================================================================================================

from rest_framework import serializers
from .models import Answer, Question, Survey, Response
from django.contrib.auth.models import User

# =============================================
# Create serializer classes that allow for exposing certain model fields to be used in the API
# =============================================


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serialises 'response', 'question', 'created', 'updated', 'body', 'lat', 'lon' 
    fields of the Answer model for the API.
    """

    class Meta:
        model = Answer
        fields = ("response", "question", "created", "updated", "body", "lat", "lon")


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serialises 'text', 'order', 'required', 'question_type', 'choices'
    fields of the Question model for the API.
    """

    class Meta:
        model = Question
        fields = ("text", "order", "required", "question_type", "choices")


class ResponseSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serialises 'created', 'updated', 'survey', 'interview_uuid', 'user'
    fields of the Response model for the API.
    """

    class Meta:
        model = Response
        fields = ("created", "updated", "survey", "interview_uuid", "user")


class SurveySerializer(serializers.HyperlinkedModelSerializer):
    """
    Serialises 'id', 'name', 'description', 'is_published', 'need_logged_user',
    'editable_answers', 'display_method', 'template', 'publish_date', 
    'expire_date', 'redirect_url' fields of the Survey model for the API.
    """

    class Meta:
        model = Survey
        fields = (
            "id",
            "name",
            "description",
            "is_published",
            "need_logged_user",
            "editable_answers",
            "display_method",
            "template",
            "publish_date",
            "expire_date",
            "redirect_url",
        )


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serialises 'id', 'username', 'first_name', 'last_name', 'email'
    fields of the User model for the API.
    """

    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "email")
