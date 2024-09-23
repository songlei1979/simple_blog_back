from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


def isAuthor(request):
    if 'author' in request.user.groups.all().values_list('name', flat=True):
        return True
    return False
