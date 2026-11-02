
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password
from django.db import IntegrityError
from django.views.decorators.http import require_POST

from .models import Users


def signup(request):

    if request.method == "POST":

        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip().lower()
        phone = request.POST.get("phone", "").strip()
        role = request.POST.get("role", "")
        company_name = request.POST.get("company_name", "").strip()
        provider_type = request.POST.get("provider_type", "").strip()
        password = request.POST.get("password", "")
        confirm_password = request.POST.get("confirm_password", "")

        if not all([name, email, phone, role, password]):
            messages.error(request, "All required fields must be filled")
            return redirect("signup")

        if role not in ["Customer", "Provider"]:
            messages.error(request, "Invalid role")
            return redirect("signup")

        if role == "Provider" and not company_name:
            messages.error(request, "Company name is required")
            return redirect("signup")

        if not (phone.isascii() and phone.isdigit()
                and len(phone) == 10):
            messages.error(request, "Enter a valid 10-digit phone number")
            return redirect("signup")

        if len(password) < 8:
            messages.error(request, "Password must have at least 8 characters")
            return redirect("signup")

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect("signup")

        if Users.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect("signup")

        if Users.objects.filter(phone=phone).exists():
            messages.error(request, "Phone number already registered")
            return redirect("signup")
        
        if role == "Provider":
          if provider_type not in ["Flight", "Hotel", "Cab"]:
           messages.error(request, "Select a valid provider type")
           return redirect("signup")

        try:
            Users.objects.create(
                name=name,
                email=email,
                phone=phone,
                role=role,
                provider_company_name=company_name if role == "Provider" else None,
                provider_type=provider_type if role == "Provider" else None,
                password=make_password(password)
            )
        except IntegrityError:
            messages.error(request, "Email or phone already registered")
            return redirect("signup")

        messages.success(request, "Account created successfully")
        return redirect("signup")

    return render(request, "signup.html")

def login(request):
         if request.method == "POST":
            return redirect("home")
         return render(request, "login.html")
# LOGIN
def login_view(request):

    if request.session.get('user_id'):
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')

        # Find the user by email
        user = Users.objects.filter(email__iexact=email).first()

        # Check email and password
        if user and check_password(password, user.password):

            # Store user information in session
            request.session.cycle_key()
            request.session['user_id'] = user.user_id
            request.session['role'] = user.role

            messages.success(request, 'Login successful! Welcome to TravelGo.')

            # Redirect to home page
            return redirect('home')

        else:
            messages.error(request, 'Invalid email or password.')

    return render(request, 'login.html')


# USER PROFILE
def profile_view(request):

    user_id = request.session.get('user_id')

    # Check whether the user is logged in
    if not user_id:
        messages.error(request, 'Please login to view your profile.')
        return redirect('login')

    # Fetch the logged-in user's details
    user = get_object_or_404(
        Users,
        user_id=user_id
    )

    return render(
        request,
        'profile.html',
        {'user': user}
    )


# LOGOUT
@require_POST
def logout_view(request):

    # Remove the logged-in user's session
    request.session.flush()

    messages.success(request, 'You have logged out successfully.')

    return redirect('home')
