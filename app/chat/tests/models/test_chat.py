from django.test import TestCase
from django.core.exceptions import ValidationError

from chat.models.chat import Chat


class ChatTests(TestCase):
    def test_chat_title_not_blank(self):
        title = ""
        chat = Chat(title=title)

        with self.assertRaises(ValidationError):
            chat.full_clean()