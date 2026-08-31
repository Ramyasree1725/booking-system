from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ResourceCategoryViewSet, ResourceViewSet, AvailabilityRuleViewSet, BlackoutDateViewSet

router = DefaultRouter()
router.register('categories', ResourceCategoryViewSet, basename='category')
router.register('resources', ResourceViewSet, basename='resource')
router.register('availability-rules', AvailabilityRuleViewSet, basename='availability-rule')
router.register('blackouts', BlackoutDateViewSet, basename='blackout')

urlpatterns = [
    path('', include(router.urls)),
]
