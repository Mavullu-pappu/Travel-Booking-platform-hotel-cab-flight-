from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError
from .models import Users
# Create your views here.
def cabs(request):
         if request.method == "POST":
            return redirect("cabs")
         return render(request, "cabs.html")