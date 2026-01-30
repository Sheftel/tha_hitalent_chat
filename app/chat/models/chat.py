from django.db import models

from chat.models.base import BaseModel


class Chat(BaseModel):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return 'Chat %d: %s' % (self.id, self.title)

    def clean(self):
        if self.title:
            self.title = self.title.strip()