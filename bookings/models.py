from django.db import models
class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    total_seats = models.PositiveIntegerField()
    def __str__(self):
        return self.name
class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name = 'bookings')
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    seats_booked = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.event.name}"