from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import GetWeatherViewSet

router = DefaultRouter()
router.register(r'weather',
                GetWeatherViewSet, basename='weather')

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
]
