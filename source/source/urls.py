from django.contrib import admin
from django.urls import path, include, re_path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('djoser.urls')),
    path('api/', include('users.urls')),
    path('api/', include('billboard.urls')),
    path('chat/', include('chat.urls')),
]
