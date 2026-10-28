from django.db import models
from accounts.models import Users
from cabs.models import Cabs
from flights.models import flights
from hotels.models import Hotels
from django.db.models import Q,F

# Create your models here.
class bookings(models.Model):
    BOOKING_TYPES = [
        ("Flight", "Flight"),
        ("Hotel", "Hotel"),
        ("Cab", "Cab"),
    ]

    BOOKING_STATUS = [
        ("Pending", "Pending"),
        ("Confirmed", "Confirmed"),
        ("Cancelled", "Cancelled"),
    ]
    booking_id=models.AutoField(primary_key=True)
    user_id=models.ForeignKey(Users,on_delete=models.PROTECT,
                              related_name="customer_bookings")
    provider_id=models.ForeignKey(Users,on_delete=models.PROTECT,
                                  related_name="provider_bookings")
    flight_id=models.ForeignKey(flights,on_delete=models.PROTECT,
                                to_field="flight_id",null=True,blank=True)
    hotel_id=models.ForeignKey(Hotels,on_delete=models.PROTECT,
                               to_field="hotel_id",null=True,blank=True)
    cabs_id=models.ForeignKey(Cabs,on_delete=models.PROTECT,
                              to_field="cab_id",null=True,blank=True)
    booking_type=models.CharField(max_length=20,choices=BOOKING_TYPES)
    booking_date=models.DateTimeField(auto_now_add=True)
    total_amount=models.DecimalField(max_digits=10,decimal_places=2)
    booking_status=models.CharField(max_length=30,null=True,choices=BOOKING_STATUS,default="Pending")
    payment_method=models.CharField( max_length=30,null=True,blank=True)
    payment_amount=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    payment_status=models.CharField(max_length=20,null=True,default="Pending")
    transaction_id=models.CharField(max_length=100,null=True,unique=True,blank=True)
    payment_date=models.DateTimeField(null=True,blank=True)
    cancelled_by=models.ForeignKey(Users,on_delete=models.PROTECT,
                                   related_name="cancelled_bookings",null=True,blank=True)
    cancellation_reason=models.CharField(max_length=255,null=True,blank=True)
    refund_amount=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    cancellation_status=models.CharField(max_length=20,null=True,blank=True)
    cancelled_at=models.DateTimeField(null=True,blank=True)
    
    def __str__(self):
        return f"Booking {self.booking_id} - {self.booking_type}"
    
    
