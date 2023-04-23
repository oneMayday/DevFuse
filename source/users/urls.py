from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.views import ProfileView

router = DefaultRouter()
router.register(r'profile', ProfileView, basename='profile')


urlpatterns = [
    path('', include(router.urls)),
]
