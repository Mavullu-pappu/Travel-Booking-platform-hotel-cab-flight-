from django.db import models
from accounts.models import Users
from django.db.models import Q,F

# Create your models here.
class flights(models.Model):
    flight_id=models.AutoField(primary_key=True)
    flight_name=models.CharField(max_length=100)
    provider_id=models.ForeignKey(Users,on_delete=models.CASCADE,
                                  to_field="user_id")
    flight_number=models.CharField(max_length=20,unique=True)
    source=models.CharField(max_length=100)
    destination=models.CharField(max_length=100)
    departure_time=models.DateTimeField()
    arrival_time=models.DateTimeField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    total_seats=models.PositiveIntegerField()
    available_seats=models.PositiveIntegerField()
    
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
    
    class Meta:
     constraints = [
        models.CheckConstraint(
            condition=Q(price__gte=0),
            name="flight_price_positive"
        ),
        models.CheckConstraint(
            condition=Q(
                available_seats__lte=F("total_seats")
            ),
            name="valid_available_seats"
        ),
        models.CheckConstraint(
            condition=Q(
                arrival_time__gt=F("departure_time")
            ),
            name="valid_flight_time"
        ),
    ]