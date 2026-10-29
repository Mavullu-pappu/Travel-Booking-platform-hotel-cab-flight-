from django.shortcuts import render,redirect

# Create your views here.


def hotels(request):
    return render(request,'hotels.html')
