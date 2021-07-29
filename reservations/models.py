from django.db import models
from django.utils import timezone  # to use  server time for each location in the users
from core import models as core_models


class Reservation(core_models.TimeStampedModel):
    """Reservation Models Definition"""

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CANCELED, "Canceled"),
    )

    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default=STATUS_PENDING
    )
    guest = models.ForeignKey(
        "users.User", related_name="reservations", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", related_name="reservations", on_delete=models.CASCADE
    )
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self) -> str:
        return f"{self.room}-{self.check_in}"

    def in_progress(self):
        current = timezone.now().date()
        return current >= self.check_in and current <= self.check_out

    in_progress.boolean = True

    def is_finished(self):
        current = timezone.now().date()
        return current > self.check_out

    is_finished.boolean = True
