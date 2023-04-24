from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users import views


router = DefaultRouter()
router.register(r'profiles', views.ProfileAPIView, basename='profiles')
router.register(r'technologies', views.TechnologieAPIView, basename='technologies')
router.register(r'specializations', views.SpecializationAPIView, basename='specializations')

urlpatterns = [
    path('', include(router.urls)),
]
