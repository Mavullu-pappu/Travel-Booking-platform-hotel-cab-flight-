from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def cabs(request):
    return render(request,'cabs.html')
def flights(request):
    return render(request, 'flights.html')