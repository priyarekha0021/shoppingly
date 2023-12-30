from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def learn_django(request):
    return HttpResponse('hello django')

def learn_python(request):
    return HttpResponse('<h1>hello python<h1>')
def learn_var(request):
    a='<h1>hello variable<h1>'
    return HttpResponse(a)
def learn_math(request):
    a=10+10
    return HttpResponse(a)
def learn_format(request):
    a='rekha'
    return HttpResponse(f'hello how are you{a}')

