from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentRegistration
# Create your views here.
def showformdata(request):
 if request.method == 'POST':
  fm = StudentRegistration(request.POST)
  if fm.is_valid():
   print('Form Validated')
   print('Name:', fm.cleaned_data['name'])
   print('Roll:', fm.cleaned_data['roll'])
   print('Price:', fm.cleaned_data['price'])
   print('Rate:', fm.cleaned_data['rate'])
   print('Comment:', fm.cleaned_data['comment'])
   print('Email:', fm.cleaned_data['email'])
   print('Website:', fm.cleaned_data['website'])
   print('Password:', fm.cleaned_data['password'])
   print('Description:', fm.cleaned_data['description'])
   print('Feedback:', fm.cleaned_data['feedback'])
   print('Notes:', fm.cleaned_data['notes'])
   print('Agree:', fm.cleaned_data['agree'])
   
 else:
  fm = StudentRegistration()

 return render(request, 'enroll/userregistration.html', {'form':fm})
