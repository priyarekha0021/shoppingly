from django.core import validators
from django import forms
class StudentRegistration(forms.Form):
 name = forms.CharField(error_messages={'required':'Enter Your Name'})
 email = forms.EmailField(error_messages={'required':'Enter Your Email'})
 password = forms.CharField(widget=forms.PasswordInput, error_messages={'required':'Enter Your Password'}) 

