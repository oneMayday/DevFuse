from rest_framework import viewsets

from users.models import Profile
from users.serializers import ProfileSerializer


class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
