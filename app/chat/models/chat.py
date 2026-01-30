from django.db import models

from chat.models import BaseModel


class Chat(BaseModel):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, blank=False) #TODO: trim whitespaces from both ends

    def __str__(self):
        return 'Chat %d: %s' % (self.id, self.title)