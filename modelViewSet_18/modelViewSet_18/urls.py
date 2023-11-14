
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from api import views

# Create Router
router = DefaultRouter()

# Register StudentModelViewSet with Router
router.register('studentapi', views.StudentModelViewSet, basename='student')  # Ex-1
# router.register('studentapi', views.StudentReadOnlyModerViewSet, basename='student')  # Ex-2


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
