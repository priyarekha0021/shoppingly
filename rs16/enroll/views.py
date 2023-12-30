from django.shortcuts import render
from .models import Student
# Create your views here.

def studentinfo(request):
 stud = Student.objects.all()
 print('Myoutput', stud)
 return render(request, 'enroll/studetails.html', {'stu': stud})