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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_view
from django.shortcuts import render
from django.http import JsonResponse

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView


def health_check(request):
    return JsonResponse({"status": "ok"}, status=200)

def home(request):

    # if request.user.is_authenticated:
    #     access_token = request.user.socialaccount_set.get(provider='google').socialtoken_set.get().token
    #     print(access_token)

    return render(request, 'home.html')

urlpatterns = [
    path('home', home),

    path('api/admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),

    # path('', include('survey_design.urls')), # enables the survey_design (depricated) app
    path('respondent/', include('respondent.urls')),
    # path('auth/', include('users.urls')),
    path('voice/v3/', include('voice.urls')),
    path('designer/', include('survey_design.urls')),
    path('civilian/v1/', include('civilian.urls')),
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    #path('api/auth/', include('knox_allauth.urls')),
    path('voice/v3/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('voice/v3/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('health/', health_check, name="health_check"),
]

# TODO: continue here: Registering users work but the redirect page is not available. API returns success
# but frontend does not redirect to the survey page. The issue is likely in the frontend.
# error: [Vue Router warn]: No match found for location with path "/designer"

# Serve static files through Django
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
