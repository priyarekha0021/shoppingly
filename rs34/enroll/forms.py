
from django.core import validators
from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
 class Meta:
  model = User
  fields = ['name', 'password', 'email']
  labels = {'name':'Enter Name', 'password':'Enter Password', 'email': 'Enter EMail'}
  error_messages = {
   'name':{'required':'Naam Likhna Jaruri Hai'},
   'password':{'required':'Password Likhna Jaruri Hai'}
  }
  widgets = {
   'password':forms.PasswordInput,
   'name':forms.TextInput(attrs={'class':'myclass', 'placeholder':'Yaha Naam Likhiye'})
  }

