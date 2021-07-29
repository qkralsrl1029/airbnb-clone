from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom User Model"""

    # gender choice constants
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        # (what goes db , what shows in form )
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    # language choice constants
    LANGUAGE_ENGLISH = "english"
    LANGUAGE_KOREAN = "korean"
    LANGUAGE_CHINESE = "chinese"

    LANGUAGE_CHOICES = (
        # (what goes db , what shows in form )
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_KOREAN, "Korean"),
        (LANGUAGE_CHINESE, "Chinese"),
    )

    # currency choice constants
    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = (
        (CURRENCY_USD, "USD"),
        (CURRENCY_KRW, "KRW"),
    )

    avatar = models.ImageField(upload_to="avatars", blank=True)
    # blank!=null, null is also a kind of data type, balnk means empty space
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    # char==single line
    bio = models.TextField(blank=True)  # multi-line char with no limit
    birth = models.DateField(blank=True, null=True)  # date field
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=10, blank=True)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, blank=True)
    superhost = models.BooleanField(default=False)

    # Should follow the rule of django!!
