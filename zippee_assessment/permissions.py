from rest_framework import permissions    

class AdminPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'ADMIN' and request.user.is_active 
    
    def has_object_permission(self, request, view, obj):
        return request.user.role == 'ADMIN' and request.user.is_active
    

class ManagerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ['MANAGER', 'ADMIN'] and request.user.is_active 
    
    def has_object_permission(self, request, view, obj):
        return request.user.role in ['MANAGER', 'ADMIN'] and request.user.is_active
    

class UserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ['USER', 'MANAGER', 'ADMIN'] and request.user.is_active
    
    def has_object_permission(self, request, view, obj):
        return request.user.role in ['USER', 'MANAGER', 'ADMIN'] and request.user.is_active
