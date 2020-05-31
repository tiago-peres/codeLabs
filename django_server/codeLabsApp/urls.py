from django.urls import path, include
from codeLabsApp import views
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from codeLabsApp.views import MyTokenObtainPairView

router = DefaultRouter()

urlpatterns = [
    path('', views.RootView.as_view(), name='welcome'),
    path('api/',include(router.urls)),
    url(r'api/users/', views.MyUserCreate.as_view(), name='user-create'),
    
    
    # JWT Token
    #path('api/token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain'),
    # Get a new token before the old expires.
    path('api/token/refresh/', TokenRefreshView.as_view, name='token_refresh'),
    
    # Test JWT Auth
    path('api/hello/', views.HelloView.as_view(), name='hello'),

]