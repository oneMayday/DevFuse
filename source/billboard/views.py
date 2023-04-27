from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from billboard.models import Publication
from billboard.serializers import PublicationSerializer


class PublicationsAPIView(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    permission_classes = [
        IsAdminUser
    ]

