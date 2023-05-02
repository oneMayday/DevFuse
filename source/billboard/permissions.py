from rest_framework.permissions import BasePermission

from billboard.models import Publication


class IsPublicationOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        publication = Publication.objects.filter(owner_id=obj)
        return True if publication else False
