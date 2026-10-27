from django.db import models
from accounts.models import Users

# Create your models here.
class Cabs(models.Model):
    
    cab_id=models.AutoField(primary_key=True)
    provider_id=models.ForeignKey(
        Users ,on_delete=models.CASCADE,
        to_field="user_id"
    )
    vehicle_number=models.CharField(max_length=100,unique=True)
    cab_type=models.CharField(max_length=100)
    driver_name=models.CharField(max_length=50,null=False)
    driver_phone=models.BigIntegerField(null=False)
    price_per_km=models.DecimalField(max_digits=10,decimal_places=2,null=False)
    STATUS_CHOICES = [
    ("Available", "Available"),
    ("Booked", "Booked"),
    ("Inactive", "Inactive"),
]

    status = models.CharField(
    max_length=20,
    choices=STATUS_CHOICES,
    default="Available"
)
  