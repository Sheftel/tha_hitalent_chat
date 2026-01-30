from django.db.models import Prefetch

from chat.models import Chat, Message


def chat_retrieve(
    chat_id: int
) -> Chat:
    message_prefetch = Prefetch('messages', queryset=Message.objects.order_by('-created_at'))
    return Chat.objects.filter(id=chat_id).prefetch_related(message_prefetch).first()
