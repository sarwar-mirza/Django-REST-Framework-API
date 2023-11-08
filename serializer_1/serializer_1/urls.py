
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuinfo/', views.student_details, name='home'),     # Ex-1
    path('stuinfo/<int:pk>/', views.student_details_pk, name='home'), # Ex-2
    path('stulist/', views.student_list, name='stulst'),        # Ex-3
    
]
