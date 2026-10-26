from django.db import models

# Create your models here.
class Users(models.Model):
    user_id=models.AutoField(primary_key=True,null=False)
    name=models.CharField( max_length=50,null=False)
    email=models.EmailField(max_length=100,unique=True)
    password=models.CharField(max_length=10,unique=True)
    phone=models.IntegerField(unique=True)
    role=models.CharField(max_length=10)
    provider_type=models.CharField(max_length=50,null=True)
    provider_company_name=models.CharField(max_length=50,null=True)
    created_at=models.DateTimeField()
        
    
    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=models.Q(
                    role__in=['customer', 'provider']
                    
                ),
                name='check_user_role'
            ),
            models.CheckConstraint(
                condition=models.Q(
                    provider_type__in=['cabs','flights','hotels']
                    
                ),
                name='check_provider_type'
            )
        ]
        
    
    
