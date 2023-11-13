
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('studentapi/', views.StudentList.as_view()), # Ex-1
    # path('studentapi/', views.StudentCreate.as_view()), # Ex-2
    # path('studentapi/<int:pk>/', views.StudentRetrieve.as_view()), # Ex-3
    # path('studentapi/<int:pk>/', views.StudentUpdate.as_view()), # Ex-4
    # path('studentapi/<int:pk>/', views.studentDestroy.as_view()), # Ex-5
    
    path('studentapi/', views.LCStudentApi.as_view()),
    path('studentapi/<int:pk>/', views.RUDStudentApi.as_view()),
]
