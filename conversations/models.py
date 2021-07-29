from django.db import models
from core import models as core_models


class Conversation(core_models.TimeStampedModel):
    """Conversation Model Definition"""

    participants = models.ManyToManyField(
        "users.User", related_name="conversations", blank=True
    )

    def __str__(self) -> str:
        username = []
        for i in self.participants.all():
            username.append(i.username)
        return ", ".join(username)  # transform list to str

    def count_messages(self):
        return self.messages.count()

    def count_participants(self):
        return self.participants.count()


class Message(core_models.TimeStampedModel):
    message = models.TimeField()
    user = models.ForeignKey(
        "users.User", related_name="messages", on_delete=models.CASCADE
    )
    conversation = models.ForeignKey(
        "Conversation", related_name="messages", on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f"{self.user} says: {self.message}"
