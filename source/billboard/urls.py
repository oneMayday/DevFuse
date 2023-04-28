from django.urls import include, path

from rest_framework.routers import DefaultRouter

from billboard import views


router = DefaultRouter()
router.register('billboard', views.PublicationsAPIView, basename='billboard')

urlpatterns = [
    path('', include(router.urls))
]
