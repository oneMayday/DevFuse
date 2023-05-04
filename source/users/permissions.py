from rest_framework.permissions import BasePermission, IsAdminUser


class IsProfileOwnerOrAdminOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return any([bool(request.user and request.user.is_staff), request.user == obj.user])
