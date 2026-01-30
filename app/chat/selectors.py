from chat.models import Chat



def chat_retrieve(
    chat_id: int
) -> Chat:
    return Chat.object.get(id=chat_id).prefetch_related('messages').first()

