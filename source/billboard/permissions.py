from rest_framework.permissions import BasePermission


class IsPublicationOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner


class IsInTeam(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user in obj.team.all()
