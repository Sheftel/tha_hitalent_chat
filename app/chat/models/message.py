from django.db import models

from chat.models.base import BaseModel
from chat.models.chat import  Chat


class Message(BaseModel):
    id = models.AutoField(primary_key=True)
    text = models.TextField(max_length=5000, blank=False)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')

    def __str__(self):
        return 'Message %d: %s' % (self.id, self.text)