
"""Role and object-level permission classes for the booking API."""
from __future__ import annotations

from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminRole(BasePermission):
    """Allow only users with admin role or superuser."""

    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False
        return getattr(user, "is_admin_role", False) or user.is_superuser


class IsStaffRole(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False
        return getattr(user, "is_staff_role", False) or user.is_staff or user.is_superuser


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        user = request.user
        return bool(user and user.is_authenticated and (getattr(user, "is_admin_role", False) or user.is_staff))


class IsOwnerOrStaff(BasePermission):
    owner_field = "user"

    def has_object_permission(self, request, view, obj):
        user = request.user
        if not user or not user.is_authenticated:
            return False
        if user.is_staff or getattr(user, "is_admin_role", False):
            return True
        owner = getattr(obj, self.owner_field, None)
        if owner is None:
            return False
        owner_id = owner.pk if hasattr(owner, "pk") else owner
        return owner_id == user.pk


class IsOwnerOrReadOnly(BasePermission):
    owner_field = "user"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        user = request.user
        if not user or not user.is_authenticated:
            return False
        if user.is_staff or getattr(user, "is_admin_role", False):
            return True
        owner = getattr(obj, self.owner_field, None)
        owner_id = owner.pk if hasattr(owner, "pk") else owner
        return owner_id == user.pk


class CanManageResource(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        if not user or not user.is_authenticated:
            return False
        if user.is_staff or getattr(user, "is_admin_role", False):
            return True
        created_by = getattr(obj, "created_by_id", None)
        return created_by == user.pk


class CanApproveBooking(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return bool(user and user.is_authenticated and (user.is_staff or getattr(user, "is_admin_role", False)))


class HasVerifiedEmail(BasePermission):
    message = "Email verification required."

    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False
        return getattr(user, "is_verified", True)


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
