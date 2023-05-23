from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from users.models import Profile, Technologie, Specialization
from users.permissions import IsProfileOwnerOrAdminOrReadOnly
from users.serializers import (TechnologieSerializer,
                               SpecializationSerializer,
                               CreateAndUpdateProfileSerializer,
                               ReadProfileSerializer
                               )


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

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            serializer_class = ReadProfileSerializer
        else:
            serializer_class = CreateAndUpdateProfileSerializer
        return serializer_class

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsProfileOwnerOrAdminOrReadOnly]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
