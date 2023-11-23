from django.urls import path, include
from rest_framework.routers import DefaultRouter

from enroll.api import views      # package.folder_name import views

# Create Router
router = DefaultRouter()

# Register StudentModelViewSet with ROUTER
router.register('crudapi', views.StudentModelViewSet, basename='crud')

urlpatterns = [
    path('', include(router.urls)),
]


