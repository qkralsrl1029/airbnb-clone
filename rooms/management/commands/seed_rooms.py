import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from rooms import models as rooms_models
from users import models as user_models

# https://docs.djangoproject.com/en/3.2/howto/custom-management-commands/


class Command(BaseCommand):
    help = "This command creates fake users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help="How many users do you want to create?",
        )

    # create dummy room
    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        room_types = rooms_models.RoomType.objects.all()
        seeder.add_entity(
            rooms_models.Room,
            number,
            {
                # write the part where faker cannot automatically fill(FK)
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(room_types),
                "guests": lambda x: random.randint(1, 20),
                "price": lambda x: random.randint(1, 300),
                "beds": lambda x: random.randint(1, 5),
                "bedrooms": lambda x: random.randint(1, 5),
                "baths": lambda x: random.randint(1, 5),
            },
        )
        created_photos = seeder.execute()  # return primary keyes
        created_clean = flatten(
            list(created_photos.values())
        )  # linielization, make double dimension arr to list
        amenities = rooms_models.Amenity.objects.all()
        facilities = rooms_models.Facility.objects.all()
        rules = rooms_models.HouseRule.objects.all()
        for pk in created_clean:
            room = rooms_models.Room.objects.get(pk=pk)
            for i in range(3, random.randint(6, 9)):
                # create random number of photoes for rooms
                rooms_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room,
                    file=f"room_photos/{random.randint(1, 8)}.jpg",
                )
        for a in amenities:
            rand = random.randint(0, 15)
            if rand % 2 == 0:
                room.amenities.add(a)
        for f in facilities:
            rand = random.randint(0, 15)
            if rand % 2 == 0:
                room.facilities.add(f)
        for r in rules:
            rand = random.randint(0, 15)
            if rand % 2 == 0:
                room.house_rules.add(r)
        self.stdout.write(self.style.SUCCESS("rooms created"))
