from django import forms
class StudentRegistration(forms.Form):
 name = forms.CharField(widget=forms.PasswordInput)
 email = forms.EmailField(widget=forms.FileInput)
 mobile = forms.IntegerField(widget=forms.Textarea)
     
 