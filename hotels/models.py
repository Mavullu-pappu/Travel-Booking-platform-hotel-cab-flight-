from django.db import models
from accounts.models import Users
from django.db.models import Q,F


# Create your models here.
class Hotels(models.Model):
    hotel_id=models.AutoField(primary_key=True)
    provider_id=models.ForeignKey(Users,on_delete=models.CASCADE,
                                 to_field="user_id")
    hotel_name=models.CharField(max_length=150)
    location=models.CharField(max_length=150)
    address=models.CharField(max_length=255)
    phone=models.BigIntegerField()
    room_type=models.CharField(max_length=50)
    price_per_day=models.DecimalField(max_digits=10,decimal_places=2)
    capacity=models.PositiveIntegerField()
    rating=models.DecimalField(max_digits=2,decimal_places=1)
    available_rooms=models.PositiveIntegerField()
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
                condition=Q(price_per_day__gte=0),
                name="hotel_price_positive"
            ),
            models.CheckConstraint(
                condition=Q(rating__gte=0) & Q(rating__lte=5),
                name="hotel_rating_range"
            ),
        ]

    def __str__(self):
        return self.hotel_name
