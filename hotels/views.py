from django.core.checks import messages
from django.shortcuts import render,redirect

# Create your views here.


def hotels(request):
    if not request.session.get('user_id'):
        messages.error(request, "Please log in to access this page.")
        return redirect("login")
    if request.method == "POST":
          return redirect("hotels")
    return render(request,'hotels.html')
