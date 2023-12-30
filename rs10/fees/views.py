from django.shortcuts import render

# Create your views here.
def fees_django(request):
  return render(request, 'fees/feesone.html', {'title':'Django Fees', 'cname':'Django', 'charge':300})