from django.contrib import admin
from django.utils.html import mark_safe

# to ensure to system that the format using for image is safe
from . import models


class PhotoInline(admin.TabularInline):
    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """Room Admin Definition"""

    inlines = (PhotoInline,)  # inline field to use photo in room app

    fieldsets = (
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")}),
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "city", "price")},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        (
            "More About the Spaces",
            {
                "classes": ("collapse",),  # can fold the information
                "fields": ("amenities", "facilities", "house_rules"),
            },
        ),
        ("Last Details", {"fields": ("host",)}),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",  # can display return value of function
        "count_photoes",
        "total_rating",
    )

    list_filter = (
        "instant_book",
        "host__superhost",  # can filter also by foreign key
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",
    )

    ordering = (
        "name",
        "price",
    )  # make order priority

    filter_horizontal = (  # filter for n-n relationships
        "amenities",
        "facilities",
        "house_rules",
    )

    raw_id_fields = ("host",)  # give opportunity to search foreign key easier

    search_fields = (
        "=city",
        "host__username",
    )  # put the search bar by exact city name & can access to foreign key

    def count_amenities(self, obj):  # self==RoomAdmin class, obj==current obj(row)
        return obj.amenities.count()

    def count_photoes(self, obj):
        return obj.photoes.count()


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """Item Admin Definition"""

    list_display = (
        "name",
        "used_by",
    )

    def used_by(self, obj):
        return obj.rooms.count()

    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Photo admin Definition"""

    list_display = (
        "__str__",
        "get_thumbnail",
    )

    def get_thumbnail(self, obj):
        return mark_safe(
            f'<img width="100pc" src="{obj.file.url}"/>'
        )  # return the html format thumbnail img

    get_thumbnail.short_description = "Thumbnail"
