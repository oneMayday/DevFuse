from django.urls import path

from chat import views


urlpatterns = [
    path('', views.room_choice, name='room-choice'),
    path('<str:room_name>/', views.room, name='room'),
]