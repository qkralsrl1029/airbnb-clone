from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):
    help = "This command creates facilities"

    def handle(self, *args, **options):

        facilities = [
            "Private Enterance",
            "Paid Parking on Premises",
            "Paid parking off Premises",
            "Elevator",
            "Parking",
            "Gym",
        ]
        for i in facilities:
            Facility.objects.create(name=i)
        # self.stdout.write(self.style.SUCCESS(f'{len(facilities)} facilities created!'))
        # return super().handle(*args, **options)
