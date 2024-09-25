from django.db import models
from django.utils import timezone
import uuid

class Bus(models.Model):
    destination = models.CharField(max_length=100)
    date = models.DateField()
    departure_time = models.TimeField()
    number_plate = models.CharField(max_length=15)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.destination} ({self.number_plate})"

class Seat(models.Model):
    seat_number = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return self.seat_number

class Booking(models.Model):
    receipt = models.CharField(max_length=50, unique=True, default=uuid.uuid4)
    date = models.DateField(default=timezone.now)
    departure_time = models.TimeField()
    destination = models.CharField(max_length=100)
    seat_number = models.ForeignKey(Seat, on_delete=models.CASCADE)
    passenger = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    number_plate = models.CharField(max_length=15)

    def save(self, *args, **kwargs):
        if not self.receipt:
            self.receipt = str(uuid.uuid4())
        if not self.amount:
            self.amount = self.price + 1300
        super().save(*args, **kwargs)
