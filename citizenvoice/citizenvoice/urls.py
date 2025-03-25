"""citizenvoice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_view
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('survey_design.urls')), # enables the survey_design (depricated) app
    path('respondent/', include('respondent.urls')),
    path('auth/', include('users.urls')),
    path('api/v2/', include('apiapp.urls')),
    path('civilian/v1/', include('civilian.urls')),
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path(r'api/auth/', include('knox_allauth.urls')),
    path('api/v2/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/v2/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
