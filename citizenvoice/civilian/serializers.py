"""
Serializers for the API endpoints of the dashboard app.
"""

import copy
from rest_framework import serializers
from apiapp.models import (Answer, Question, Survey, PointFeature, 
                     PolygonFeature, LineFeature, MapView,
                    LocationCollection, DashboardTopic)
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class DashboardTopicSerializer(serializers.ModelSerializer):
    """
    A serializer class for the DashboardTopic model.
    """
    
    class Meta:
        model = DashboardTopic
        fields = ['id','name']

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializes 'text', 'order', 'required', 'question_type', 'choices', 'is_geospatial', 'map_view'
    fields of the Question model for the API.
    """
    survey = serializers.HyperlinkedRelatedField(view_name='survey-detail',read_only=True)
    topics = serializers.SerializerMethodField(read_only=True)


    class Meta:
        model = Question
        fields = ['id', 'text', 'has_text_input', 'question_type',
                  'choices', 'survey', 'is_geospatial', 'topics']
        read_only_fields = ['id', 'url', 'text', 'explanation', 'has_text_input', 'order', 'required', 'question_type',
                  'choices', 'survey', 'is_geospatial']

    def get_topics(self, obj) -> list:
        """
        Returns a list of topic names associated with the question.
        """
        topics = DashboardTopicSerializer(DashboardTopic.objects.filter(question__id=obj.pk), 
                                       many=True,
                                       context={'request': self.context.get('request')}).data
        topic_names = [topic['name'] for topic in topics]
        return topic_names

class PointFeatureSerializer(GeoFeatureModelSerializer):
    """
    GeoJson serializer for 'id', 'url', 'geom', 'name', 'annotation', 'location' 
    fields of the PointLocation model for the API.
    """
    # location = serializers.HyperlinkedRelatedField(queryset=LocationCollection.objects.all(),
    #                                                view_name='locationcollection-detail')

    class Meta:
        model = PointFeature
        geo_field = 'geom'
        fields = ['id', 'annotation', 'geom']
        read_only_fields = ['id', 'url']
    

class PolygonFeatureSerializer(GeoFeatureModelSerializer):
    """
    GeoJson serializer for 'id', 'geom', 'annotation', 'location' fields of the PolygonLocation model for the API.
    The 'geom' field is serialized as a GeoJSON field.
    """
    # location = serializers.HyperlinkedRelatedField(queryset=LocationCollection.objects.all(),
    #                                                view_name='locationcollection-detail')

    class Meta:
        model = PolygonFeature
        geo_field = 'geom'
        fields = ['id', 'annotation', 'geom']
        read_only_fields = ['id', 'url']
    

class LineFeatureSerializer(GeoFeatureModelSerializer):
    """
    Serialises 'id', 'geom', 'annotation' fields of the LineStringLocation model for the API.
    The 'geom' field is serialized as a GeoJSON field.
    """
    # location = serializers.HyperlinkedRelatedField(queryset=LocationCollection.objects.all(),
    #                                                view_name='locationcollection-detail')

    class Meta:
        model = LineFeature
        geo_field = 'geom'
        fields = ['id', 'annotation',  'geom']
        read_only_fields = ['id', 'url']
    

class LocationsSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serialises 'name', 'question', 'answer', 'points', 'lines', 'polygons'
    fields of the Location model for the API.
    """

    geojson = serializers.SerializerMethodField()

    class Meta:
        model = LocationCollection
        fields = ['geojson']
        read_only_fields = ['id', 'url', 'name', 'description', 'geojson']
    
    def get_geojson(self, obj) -> dict:
        """
        Returns a list of features (points, lines, polygons)
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

class DashboardMapViewSerializer(serializers.ModelSerializer):
    """
    A serializer class for the MapView model used in the dashboard endpoint.
    """

    location = LocationsSerializer()

    class Meta:
        model = MapView
        fields = ['location']
        depth = 2


class DashboardAnswerSerializer(serializers.ModelSerializer):
    """
    A serializer class for the Answer model that serializes the 'geom' field as a GeoJSON field.
    """

    # response = serializers.HyperlinkedRelatedField(queryset=ResponseModel.objects.all(),view_name='response-detail')
    question = serializers.SerializerMethodField()
    mapview = DashboardMapViewSerializer()

    class Meta:
        model = Answer
        geo_field = None
        fields = ('id',  'created', 'body', 'question', 'mapview')
        read_only_fields = ('id', 'created')
        depth = 2
    
    def get_question(self, obj) -> dict:
        serializer = QuestionSerializer(Question.objects.filter(answer__id=obj.pk), 
                                       many=True,
                                       context={'request': self.context.get('request')}).data
        
        extracted_items = ['text', 'topics'] # this items will be part of the serialized data
        serializer = {key: value for key, value in serializer[0].items() if key in extracted_items}
        return serializer
    

    
