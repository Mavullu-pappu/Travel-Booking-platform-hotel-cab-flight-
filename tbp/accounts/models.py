from django.db import models
from django.db.models import Q

# Create your models here.
class Users(models.Model):
    user_id=models.AutoField(primary_key=True)
    name=models.CharField( max_length=50,null=False)
    email=models.EmailField(max_length=100,unique=True)
    password=models.CharField(max_length=128)
    phone=models.CharField(max_length=15,unique=True)
    role=models.CharField(max_length=10)
    provider_type=models.CharField(max_length=50,null=True,blank=True)
    provider_company_name=models.CharField(max_length=50,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
        
    
    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=Q(
                    role__in=['customer', 'provider']
                    
                ),
                name='check_user_role'
            ),
            models.CheckConstraint(
                condition=(
                   Q(provider_type__in=['cabs','flights','hotels']
                    
                ) |
                  Q(provider_type__isnull=True)
                ),
            
                name='check_provider_type'
            )
        ]
        
    
    
