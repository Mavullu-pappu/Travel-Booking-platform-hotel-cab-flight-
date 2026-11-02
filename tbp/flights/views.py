from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError
from .models import Users
# Create your views here.
def flights(request):
   if not request.session.get('user_id'):
      messages.error(request, "Please log in to access this page.")
      return redirect("login")

   if request.method == "POST":
      return redirect("flights")
   return render(request, "flights.html")


