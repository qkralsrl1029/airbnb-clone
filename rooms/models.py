from django.db import models
from django.urls import reverse
from django.db.models.deletion import SET_NULL
from core import models as core_models  # import from abstract class, timestamp format
from django_countries.fields import CountryField
from users import models as user_models


class AbstractItem(core_models.TimeStampedModel):
    """Abstract Item"""

    name = models.CharField(max_length=80)

    class Meta:  # make abstract class
        abstract = True

    def __str__(self) -> str:
        return self.name


# to make as model entity so that user can revise in admin pannel, different with 'choices'
class RoomType(AbstractItem):
    class Meta:
        verbose_name_plural = "Room Types"  # set plural name seen in admin pannel
        ordering = ["name"]


class Amenity(AbstractItem):
    class Meta:
        verbose_name_plural = "Amenities"  # set plural name seen in admin pannel


class Facility(AbstractItem):
    class Meta:
        verbose_name_plural = "Facilities"  # set plural name seen in admin pannel


class HouseRule(AbstractItem):
    class Meta:
        verbose_name_plural = "House Rules"  # set plural name seen in admin pannel


class Room(core_models.TimeStampedModel):
    """Room Model Definition"""

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    guests = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(
        user_models.User, related_name="rooms", on_delete=models.CASCADE
    )
    # foreign key reference, 1 - n
    room_type = models.ForeignKey(
        RoomType, related_name="rooms", on_delete=models.SET_NULL, null=True
    )
    # foreign key reference, 1 - n
    amenities = models.ManyToManyField(Amenity, related_name="rooms", blank=True)
    facilities = models.ManyToManyField(Facility, related_name="rooms", blank=True)
    house_rules = models.ManyToManyField(HouseRule, related_name="rooms", blank=True)
    # foreign key reference, n - n

    def __str__(self) -> str:
        return self.name

    def save(
        self, *args, **kwargs
    ):  # override save func, intercept the saved data when saving
        self.city = self.city.title()  # additional feature
        super().save(*args, **kwargs)  # super class save function

    def get_absolute_url(self):
        return reverse("rooms:detail", kwargs={"pk": self.pk})

    def total_rating(self):
        total = self.reviews.all()
        sum = 0
        if len(total) > 0:
            for review in total:
                sum += review.rating_average()
            return round(sum / self.reviews.count(), 2)


class Photo(core_models.TimeStampedModel):
    """Photo model definition"""

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="room_photos")
    room = models.ForeignKey(
        "Room", related_name="photoes", on_delete=models.CASCADE
    )  # can refer by using string, not class name

    def __str__(self) -> str:
        return self.caption
