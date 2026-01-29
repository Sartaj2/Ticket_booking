from django.core.exceptions import ValidationError
from decimal import Decimal
from .models import Event, Booking

class BookingService:
    def create_booking(self, event_id: int, customer_name: str, email: str, seats: int) -> Booking:
        try:
            event = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            raise ValidationError("Event does not exists")

        curr_booking = sum(b.seats for b in event.bookings.all())
        if curr_booking + seats > event.seats:
            raise ValidationError("Not enough seats")

        price_per_seats = Decimal("100.00")
        total_price = price_per_seats * seats

        booking = Booking.objecta.create(
            customer_name=customer_name,
            customer_email=email,
            seats_booked=seats,
            total_price=total_price
        )
        return booking