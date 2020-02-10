from rest_framework import permissions

class StandardPermission(permissions.BasePermission):
    """
        list、retrieve　不用验证身份
        create、update、partial_update、destroy 要验证身份
    """    
    def has_permission(self, request, view):
        if view.action in ('create', 'update', 'partial_update', 'destroy'):
            print(bool(request.user and request.user.is_authenticated))
            return bool(request.user and request.user.is_authenticated)
        return True