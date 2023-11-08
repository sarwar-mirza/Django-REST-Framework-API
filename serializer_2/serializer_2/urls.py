
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuinfo/<int:pk>/', views.student_details, name='stuinfo'),
    path('stulst/', views.student_list, name='stulst'),
]
