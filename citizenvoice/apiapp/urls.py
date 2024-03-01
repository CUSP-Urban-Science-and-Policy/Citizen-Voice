# ====================================================================================================================
#
# Created with reference "Build a REST API in 30 minutes with Django REST Framework" by Bennett Garner, May 17, 2019
# https://medium.com/swlh/build-your-first-rest-api-with-django-rest-framework-e394e39a482c
#
# ====================================================================================================================

from django.urls import include, path
from rest_framework import routers, renderers
from . import views

# Render viewsets
# survey_list = views.SurveyViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })

# Create a router object and point it to the model viewsets, allowing the API to be called through the given URL addresses
router = routers.DefaultRouter()
router.register(r'answers', views.AnswerViewSet, basename='answer')
router.register(r'questions', views.QuestionViewSet, basename='question')
router.register(r'surveys', views.SurveyViewSet, basename='survey')
router.register(r'responses', views.ResponseViewSet, basename='response')
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'pointlocations', views.PointLocationViewSet,
                basename='pointlocation')
router.register(r'polygonlocations', views.PolygonLocationViewSet,
                basename='polygonlocation')
router.register(r'linestringlocations',
                views.LineStringLocationViewSet, basename='linestringlocation')
router.register(r'map_views', views.MapViewViewSet, basename='mapview')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('csrf/', views.get_csrf_token, name='get_csrf_token'),
]
