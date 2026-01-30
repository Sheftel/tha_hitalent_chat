from django.test import TestCase
from django.core.exceptions import ValidationError

from chat.models.message import Message


class MessageTests(TestCase):
    def test_message_text_not_blank(self):
        text = ""
        message = Message(text=text)

        with self.assertRaises(ValidationError):
            message.full_clean()