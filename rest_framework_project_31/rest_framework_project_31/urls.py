
from django.contrib import admin
from django.urls import path, include
from enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeStudentTemplateView.as_view(), name='home'),
    path('dashboard/', include('enroll.urls')),
    path('api/', include('enroll.api.urls')),
]
