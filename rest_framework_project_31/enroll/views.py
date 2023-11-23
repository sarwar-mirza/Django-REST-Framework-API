from django.shortcuts import render
from django.views.generic.base import TemplateView, View, RedirectView
from .forms import StudentRegistrationForm, ContactForm
from .models import Student
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView

# Create your views here.
class HomeStudentTemplateView(TemplateView):
    template_name = 'enroll/registration.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fm = StudentRegistrationForm()
        
        context = {'form': fm}
        return context
    
    def post(self, request):
        fm = StudentRegistrationForm(request.POST)
        
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            rl = fm.cleaned_data['roll']
            dp = fm.cleaned_data['department']
            ct = fm.cleaned_data['city']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            
            reg = Student(name=nm, roll=rl, department=dp, city=ct, email=em, password=pw)
            reg.save()
            messages.success(request, 'Your Registration Successfully !!!')
            
            fm = StudentRegistrationForm()
        return render(request, 'enroll/registration.html', {'form':fm})



class StudentDatabaseList(ListView):
    
    model = Student
    template_name = 'enroll/database.html'
    context_object_name = 'students'
    

class SpecificStudentDetailView(DetailView):
    model = Student
    template_name = 'enroll/detail.html'
    context_object_name = 'stu'


class StudentUpdateView(View):
    def get(self, request, id):
        pi = Student.objects.get(pk=id)
        fm = StudentRegistrationForm(instance=pi)
        return render(request, 'enroll/update.html', {'form':fm})
    
    def post(self, request, id):
        pi = Student.objects.get(pk = id)
        fm = StudentRegistrationForm(request.POST, instance=pi)
        
        if fm.is_valid():
            fm.save()
            
            messages.success(request, 'Congratulation Your data successfully Updated')
        return render(request, 'enroll/update.html', {'form':fm})


class DeleteRedirectView(RedirectView):
    url = '/'
    
    def get_redirect_url(self,*args, **kwargs):
        del_id = kwargs['id']
        Student.objects.get(pk= del_id).delete()
        return super().get_redirect_url(*args, **kwargs)


class ContactFormView(FormView):
    template_name = 'enroll/contact.html'
    form_class = ContactForm
    success_url = '/dashboard/thankyou/'
    

    
    
class ThankyouTemplateView(TemplateView):
    template_name = 'enroll/thankyou.html'
