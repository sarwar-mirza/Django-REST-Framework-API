from django import forms
from .models import Student

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'roll', 'department', 'city', 'email', 'password']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'roll': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=70, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget= forms.Textarea(attrs={'class': 'form-control'}))
    
   