from django.urls import path
from .views import SignupView, UserList, UserDetail
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('', UserList.as_view(), name='users'),
    path('<int:pk>/', UserDetail.as_view(), name='single-user'),
    path('signup/', SignupView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
