from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from billboard.models import Publication
from billboard.permissions import IsPublicationOwnerOrReadOnly
from billboard.serializers import PublicationSerializer


class PublicationsAPIView(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial-update', 'delete']:
            permission_classes = [IsAuthenticated, IsPublicationOwnerOrReadOnly]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
