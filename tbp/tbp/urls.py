"""
URL configuration for tbp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views as v1
from accounts import views 
from cabs import views as v2
from flights import views as v3
from hotels import views as v4


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v1.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('cabs/', v2.cabs, name='cabs'),
    path('flights/',v3.flights,name='flights'),
    path('hotels/', v4.hotels, name='hotels'),
    
]
