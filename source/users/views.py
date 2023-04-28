from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from users.models import Profile, Technologie, Specialization
from users.serializers import ProfileSerializer, TechnologieSerializer, SpecializationSerializer


class TechnologieAPIView(viewsets.ModelViewSet):
    queryset = Technologie.objects.all()
    serializer_class = TechnologieSerializer
    permission_classes = [
        IsAdminUser
    ]


class SpecializationAPIView(viewsets.ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer
    permission_classes = [
        IsAdminUser
    ]


class ProfileAPIView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [
        IsAuthenticated
    ]
