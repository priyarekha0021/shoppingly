from django import forms
class StudentRegistration(forms.Form):
 name = forms.CharField()
 email=forms.EmailField()
 def clean(self):
  clearned_data = super().clean()
  valname = self.cleaned_data['name']
  valemail = self.cleaned_data['email']
  if len(valname) < 4:
   raise forms.ValidationError('Name should be more than or equal 4')

  if len(valemail) < 10:
   raise forms.ValidationError('Email should be more than or equal 10')

