
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from api import views

# Create router
router = DefaultRouter()

# Register StudentModelViewSet with router
router.register('studentapi', views.StudentModelViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),      # Session  authentication
]
