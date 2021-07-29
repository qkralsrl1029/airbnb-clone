from django.db import models


class TimeStampedModel(models.Model):
    """To indicate time Stamp for commmon classes"""

    created = models.DateTimeField(auto_now_add=True)
    # save the time when object created
    updated = models.DateTimeField(auto_now=True)
    # save the time when onject updated

    class Meta:
        abstract = True
        # To enroll app as abstract class so that timestamp class itself does not appear in db
