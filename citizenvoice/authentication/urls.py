# authentication/urls.py

from dj_rest_auth.jwt_auth import get_refresh_view
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView
from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView
from authentication.views import GoogleLogin

# TODO: Continue here, test this code, it also contains changes with Django Allauth

urlpatterns = [
    path("register/", RegisterView.as_view(), name="rest_register"),
    path("login/", LoginView.as_view(), name="rest_login"),
    path("logout/", LogoutView.as_view(), name="rest_logout"),
    path("user/", UserDetailsView.as_view(), name="rest_user_details"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("token/refresh/", get_refresh_view().as_view(), name="token_refresh"),
    path("google/", GoogleLogin.as_view(), name="google_login"),
]


# TODO: available ulr may change form version to version: https://github.com/iMerica/dj-rest-auth/blob/7.0.1/dj_rest_auth/urls.py

# TODO: continuhe here, google loging failed, it coulb be because app can take up to 24 hours to be approved by google, so it may not work right now
# however, the token based authentication api works, and user can be registed that way.
# learn about the the diference between token based authentication and session based authentication. Which one to use when and why
