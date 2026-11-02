from django.db import models
from django.db.models import Q

# Create your models here.
class Users(models.Model):
    PROVIDER_TYPES = [
    ("Flight", "Flight"),
    ("Hotel", "Hotel"),
    ("Cab", "Cab"),
]

    ROLS = [
    ("Provider", "provider"),
    ("Customer", "customer"),
    
]
    user_id=models.AutoField(primary_key=True)
    name=models.CharField( max_length=50,null=False)
    email=models.EmailField(max_length=100,unique=True)
    password=models.CharField(max_length=128)
    phone=models.CharField(max_length=15,unique=True)
    role=models.CharField(max_length=10,choices=ROLS)
    provider_type=models.CharField(max_length=50,null=True,blank=True,choices=PROVIDER_TYPES)
    provider_company_name=models.CharField(max_length=50,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
        
    
    