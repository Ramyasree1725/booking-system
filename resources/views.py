from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.utils.text import slugify
from .models import ResourceCategory, Resource, AvailabilityRule, BlackoutDate
from .serializers import (
    ResourceCategorySerializer, ResourceSerializer, ResourceListSerializer,
    AvailabilityRuleSerializer, BlackoutDateSerializer,
)


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated and (
            getattr(request.user, 'is_admin_role', False) or request.user.is_staff
        )


class ResourceCategoryViewSet(viewsets.ModelViewSet):
    queryset = ResourceCategory.objects.filter(is_active=True)
    serializer_class = ResourceCategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['order', 'name']


class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.select_related('category').prefetch_related('availability_rules')
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'category', 'is_public', 'requires_approval']
    search_fields = ['name', 'location', 'description']
    ordering_fields = ['name', 'capacity', 'created_at']
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'list':
            return ResourceListSerializer
        return ResourceSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_authenticated or not getattr(self.request.user, 'is_staff_role', False):
            qs = qs.filter(is_public=True, status=Resource.Status.ACTIVE)
        return qs

    def perform_create(self, serializer):
        name = serializer.validated_data['name']
        base_slug = slugify(name)
        slug = base_slug
        counter = 1
        while Resource.objects.filter(slug=slug).exists():
            slug = f'{base_slug}-{counter}'
            counter += 1
        serializer.save(created_by=self.request.user, slug=slug)

    @action(detail=True, methods=['get'])
    def availability(self, request, slug=None):
        resource = self.get_object()
        rules = AvailabilityRuleSerializer(resource.availability_rules.filter(is_active=True), many=True)
        blackouts = BlackoutDateSerializer(
            BlackoutDate.objects.filter(resource=resource) | BlackoutDate.objects.filter(resource__isnull=True),
            many=True,
        )
        return Response({
            'resource': resource.slug,
            'rules': rules.data,
            'blackouts': blackouts.data,
            'buffer_minutes': resource.buffer_minutes,
            'min_duration_minutes': resource.min_duration_minutes,
            'max_duration_minutes': resource.max_duration_minutes,
        })


class AvailabilityRuleViewSet(viewsets.ModelViewSet):
    queryset = AvailabilityRule.objects.select_related('resource')
    serializer_class = AvailabilityRuleSerializer
    permission_classes = [IsAdminOrReadOnly]
    filterset_fields = ['resource', 'weekday', 'is_active']


class BlackoutDateViewSet(viewsets.ModelViewSet):
    queryset = BlackoutDate.objects.select_related('resource')
    serializer_class = BlackoutDateSerializer
    permission_classes = [IsAdminOrReadOnly]
    filterset_fields = ['resource']
