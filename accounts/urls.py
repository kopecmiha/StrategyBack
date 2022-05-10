from django.urls import path
from .views import SignUp, GetUserProfile, ObtainToken, UpdateUserProfile

urlpatterns = [
    path('sign_up/', SignUp.as_view()),
    path('obtain_token/', ObtainToken.as_view()),
    path('get_profile/', GetUserProfile.as_view()),
    path('update_profile/', UpdateUserProfile.as_view()),
]