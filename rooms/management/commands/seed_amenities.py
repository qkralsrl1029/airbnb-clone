from django.core.management.base import BaseCommand
from rooms.models import Amenity


class Command(BaseCommand):
    help = "This command creates amenities"

    def handle(self, *args, **options):

        amenities = [
            "Kitchen",
            "Heating",
            "Air conditioning",
            "Washer",
            "Dryer",
            "Wifi",
            "Breakfast",
            "Indoor fireplace",
            "Iron",
            "Hair dryer",
            "Dedicated workspace",
            "TV",
            "Crib",
            "High chair",
            "Smoke alarm",
            "Carbon monoxide alarm",
            "Private bathroom",
            "Beachfront",
            "Waterfront",
        ]
        for i in amenities:
            Amenity.objects.create(name=i)
        self.stdout.write(self.style.SUCCESS("Amenities created!"))
        # return super().handle(*args, **options)
