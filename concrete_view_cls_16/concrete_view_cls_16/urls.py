
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Ex=-1
    # path('studentapi/', views.StudentListApi.as_view()),
    # path('studentapi/', views.StudentCreateApi.as_view()),
    # path('studentapi/<int:pk>/', views.StudentRetrieveApi.as_view()),
    # path('studentapi/<int:pk>/', views.StudentUpdateApi.as_view()),
    # path('studentapi/<int:pk>/', views.StudentDestroyApi.as_view()),
    
    # Ex-2
    path('studentapi/', views.StudentListCreateApiView.as_view()),
    path('studentapi/<int:pk>/', views.StudentRetrieveUpdateDestroy.as_view()),
    
    
]
