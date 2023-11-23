from django.urls import path
from enroll import views

urlpatterns = [
    path('database/', views.StudentDatabaseList.as_view(), name='data'),
    path('detail/<int:pk>/', views.SpecificStudentDetailView.as_view(), name='detaildata'),  # write always <int:pk>
    path('update/<int:id>/', views.StudentUpdateView.as_view(), name='updatedata'),
    path('delete/<int:id>/', views.DeleteRedirectView.as_view(), name='deletedata'),
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('thankyou/', views.ThankyouTemplateView.as_view(), name='thankyou'),
]
