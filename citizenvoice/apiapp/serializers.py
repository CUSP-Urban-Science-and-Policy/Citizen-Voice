import copy
from rest_framework import serializers
from .models import (Answer, Question, Survey, PointFeature, 
                     PolygonFeature, LineFeature, MapView,
                    LocationCollection, DashboardTopic)
from .models import Response as ResponseModel
from django.contrib.auth.models import User
from rest_framework_gis.serializers import GeoFeatureModelSerializer

# =============================================
# Create serializer classes for exposing certain model fields to be used in the API
# =============================================

    
class TopicSerializer(serializers.ModelSerializer):
    """
    A serializer class for the DashboardTopic model.
    """
    
    class Meta:
        model = DashboardTopic
        fields = ['id', 'name']
      

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializes 'text', 'order', 'required', 'question_type', 'choices', 'is_geospatial', 'map_view'
    fields of the Question model for the API.
    """
    survey = serializers.HyperlinkedRelatedField(view_name='survey-detail',read_only=True)
    topics = serializers.HyperlinkedRelatedField(view_name='topics-detail', read_only=True, many=True)

    class Meta:
        model = Question
        fields = ('id', 'url', 'text', 'explanation', 'has_text_input', 'order', 'required', 'question_type',
                  'choices', 'survey', 'is_geospatial', 'mapview', 'topics')
        read_only_fields = ('id', 'url')

    def create(self, validated_data):
        question = Question.objects.create(
            text=validated_data['text'],
            order=validated_data['order'],
            required=validated_data['required'],
            question_type=validated_data['question_type'],
            choices=validated_data.get('choices', None),
            survey=validated_data['survey'],
            is_geospatial=validated_data.get('is_geospatial', False),
             has_text_input=validated_data.get('has_text_input', True),
            mapview=validated_data.get('mapview', None),
        )
        return question


class ResponseSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializes 'response_id', 'url', 'survey', 'respondent', 'created', 'updated'
    fields of the Response model for the API.
    """
    survey = serializers.HyperlinkedRelatedField(queryset=Survey.objects.all(),view_name='survey-detail')
    respondent = serializers.HyperlinkedRelatedField(queryset=User.objects.all(),view_name='user-detail', allow_null=True)

    def get_respondent(self, User):
        return UserSerializer(User.respondent).data
   
    class Meta:
        model = ResponseModel
        fields = ('response_id', 'url', 'created', 'updated', 'survey',
                    'respondent')
        extra_kwargs = {
            'response_id': {'read_only': True},
            'url': {'read_only': True},
            'created': {'read_only': True}
        }


    def create(self, validated_data):
        response = ResponseModel.objects.create(
            **validated_data
        )
        return response


class SurveySerializer(serializers.HyperlinkedModelSerializer):
    """
    Serialises 'id', 'name', 'description', 'submit_message', 'is_published', 'need_logged_user',
    'editable_answers', 'publish_date', 'expire_date', 'public_url', 'designer'
    fields of the Survey model for the API.
    """

    designer = serializers.HyperlinkedRelatedField(view_name='user-detail',read_only=True)
    

    class Meta:
        model = Survey
        fields = ('id', 'url', 'name', 'description', 'submit_message', 'is_published', 
                  'need_logged_user', 'editable_answers',
                  'publish_date', 'expire_date', 'public_url', 'designer')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serialises 'id', 'username', 'first_name', 'last_name', 'email'
    fields of the User model for the API.
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')


class PointFeatureSerializer(GeoFeatureModelSerializer):
    """
    GeoJson serializer for 'id', 'url', 'geom', 'name', 'annotation', 'location' 
    fields of the PointLocation model for the API.
    """
    location = serializers.HyperlinkedRelatedField(queryset=LocationCollection.objects.all(),
                                                   view_name='locationcollection-detail')

    class Meta:
        model = PointFeature
        geo_field = 'geom'
        fields = ('id', 'url', 'annotation', 'location', 'geom')
        read_only_fields = ('id', 'url')
    
    def create(self, validated_data):
        response = PointFeature.objects.create(
            **validated_data
        )
        return response


class PolygonFeatureSerializer(GeoFeatureModelSerializer):
    """
    GeoJson serializer for 'id', 'geom', 'annotation', 'location' fields of the PolygonLocation model for the API.
    The 'geom' field is serialized as a GeoJSON field.
    """
    location = serializers.HyperlinkedRelatedField(queryset=LocationCollection.objects.all(),
                                                   view_name='locationcollection-detail')

    class Meta:
        model = PolygonFeature
        geo_field = 'geom'
        fields = ('id', 'url', 'annotation', 'location', 'geom')
        read_only_fields = ('id', 'url')
    
    def create(self, validated_data):
        response = PolygonFeature.objects.create(
            **validated_data
        )
        return response

class LineFeatureSerializer(GeoFeatureModelSerializer):
    """
    Serialises 'id', 'geom', 'annotation' fields of the LineStringLocation model for the API.
    The 'geom' field is serialized as a GeoJSON field.
    """
    location = serializers.HyperlinkedRelatedField(queryset=LocationCollection.objects.all(),
                                                   view_name='locationcollection-detail')

    class Meta:
        model = LineFeature
        geo_field = 'geom'
        fields = ('id', 'url', 'annotation', 'location', 'geom')
        read_only_fields = ('id', 'url')
    

    def create(self, validated_data):
        response = LineFeature.objects.create(
            **validated_data
        )
        return response


class LocationCollectionSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serialises 'name', 'question', 'answer', 'points', 'lines', 'polygons'
    fields of the Location model for the API.
    """

    geojson = serializers.SerializerMethodField()

    class Meta:
        model = LocationCollection
        fields = ('id', 'url', 'name', 'description', 'geojson')
        read_only_fields = ('id', 'url')
    
    def get_geojson(self, obj):
        """
        Returns a list of URLs of all the features (points, lines, polygons)
        associated with the location collection.
        """
        points = PointFeatureSerializer(PointFeature.objects.filter(location__id=obj.pk), 
                                       many=True,
                                       context={'request': self.context.get('request')}).data
        lines = LineFeatureSerializer(LineFeature.objects.filter(location__id=obj.pk), 
                                       many=True,
                                       context={'request': self.context.get('request')}).data
        polygons = PolygonFeatureSerializer(PolygonFeature.objects.filter(location__id=obj.pk), 
                                       many=True,
                                       context={'request': self.context.get('request')}).data
        features = copy.deepcopy(points)
        features['features'].extend(lines['features'])
        features['features'].extend(polygons['features'])

        return  features


class AnswerCSVSerializer(serializers.ModelSerializer):
    """
    Serialises 'response', 'question', 'created', 'updated', 'body'
    fields of the Answer model for the API.
    """
    response = serializers.SerializerMethodField()
    mapview = serializers.SerializerMethodField()
    question = serializers.SerializerMethodField()

    class Meta:
        model = Answer
        fields = ('id', 'created', 'updated', 'question', 'body',  'response', 'mapview')
        read_only_fields = ('id', 'created', 'updated', 'question', 'response', 'mapview')
        
    
    def get_response(self, obj):
        serializer = ResponseSerializer(obj.response, context={'request': self.context.get('request')})
        return serializer.data
    
    def get_mapview(self, obj):
        serializer = MapViewSerializer(obj.mapview, context={'request': self.context.get('request')})
        return serializer.data
    
    def get_question(self, obj):
        serializer = QuestionSerializer(obj.question, context={'request': self.context.get('request')})
        return serializer.data
    

class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serialises 'response', 'question', 'created', 'updated', 'body'
    fields of the Answer model for the API.
    """
    
    response = serializers.HyperlinkedRelatedField(queryset=ResponseModel.objects.all(),view_name='response-detail')
    mapview = serializers.HyperlinkedRelatedField(queryset=MapView.objects.all(), view_name='mapview-detail', allow_null=True)
    question = serializers.HyperlinkedRelatedField(queryset=Question.objects.all(), view_name='question-detail')
    
    class Meta:
        model = Answer
        fields = ('id', 'url', 'created', 'updated', 'body',  'question', 'response', 'mapview')
        read_only_fields = ('id', 'url', 'created')
        depth = 2

    def create(self, validated_data):
        response = Answer.objects.create(
            **validated_data
        )
        return response

class MapViewSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serialises 'name', 'map_service_url' and 'options'
    fields of the MapView model for the API.
    """
    
    class Meta:
        model = MapView
        fields = ('id', 'url', 'name', 'description', 'map_service_url', 
                  'options', 'location')
        read_only_fields = ('id', 'url')
       

    def create(self, validated_data):
        mapview = MapView.objects.create(
            **validated_data
        )
        return mapview
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.map_service_url = validated_data.get('map_service_url', instance.map_service_url)
        instance.options = validated_data.get('options', instance.options)
        instance.location = validated_data.get('location', instance.location)
        instance.save()
        return instance


