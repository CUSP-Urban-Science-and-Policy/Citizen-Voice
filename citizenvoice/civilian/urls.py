# ====================================================================================================================
#
# Created with reference "Build a REST API in 30 minutes with Django REST Framework" by Bennett Garner, May 17, 2019
# https://medium.com/swlh/build-your-first-rest-api-with-django-rest-framework-e394e39a482c
#
# ====================================================================================================================

from django.urls import include, path
from rest_framework import routers
from . import views
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView

# Dashboard viewsets
dashboard_router = routers.DefaultRouter()
dashboard_router.register(r'answers', views.AnswerGeoJsonViewSet,
                basename='answers')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(dashboard_router.urls)),
    # path('csrf/', views.get_csrf_token, name='get_csrf_token'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

