from django.db import models

from chat.models import BaseModel, Chat


class Message(BaseModel):
    id = models.AutoField(primary_key=True)
    text = models.TextField(max_length=5000, blank=False)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
