from django.shortcuts import render, redirect
from django.urls import reverse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from billboard.models import Publication
from billboard.permissions import IsPublicationOwnerOrReadOnly, IsInTeam
from billboard.serializers import PublicationSerializer


class PublicationsAPIView(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial-update', 'delete']:
            permission_classes = [IsAuthenticated, IsPublicationOwnerOrReadOnly]
        elif self.action == 'open_chat':
            permission_classes = [IsAuthenticated, IsInTeam]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    @action(detail=True, methods=['GET'])
    def open_chat(self, request, pk):
        room_chat_title = Publication.objects.get(pk=pk).title
        room_chat_name = room_chat_title + str(pk)
        return redirect(reverse('room', kwargs={'room_name': room_chat_name}))
