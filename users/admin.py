from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models  # to import custom user


@admin.register(models.User)  # decoration == "admin will control User class"
class CustomUserAdmin(UserAdmin):
    """Custom User Admin"""

    # fieldsets means set of information fields bounded by blue box
    fieldsets = UserAdmin.fieldsets
    fieldsets += (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "language",
                    "birth",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
    """
    # select which information to be displayed
    list_display = ("username", "gender", "language", "currency", "superhost")
    # make filter of users by certain information
    list_filter = ("superhost", "username")
    """
