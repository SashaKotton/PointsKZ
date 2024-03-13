from django.urls import path, include
from authorization.views import UserProfileEditView, TokenObtainPairView, TokenRefreshView, UserProfileView, UserRegisterView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('register/', UserRegisterView.as_view()),
    path('profile/', UserProfileView.as_view()),
    path('name_change/', UserProfileEditView.as_view()),
]