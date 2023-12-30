from django import forms
class StudentRegistration(forms.Form):
 name = forms.CharField(label='your name')
 email = forms.EmailField()
 mobile = forms.IntegerField()
     
 