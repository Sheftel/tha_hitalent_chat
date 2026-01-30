from chat.models import Chat, Message


def chat_create(
    title: str
) -> Chat:

    chat = Chat(title=title)
    chat.full_clean()
    chat.save()

    return chat


def message_create(
    chat_id: int,
    text: str,
) -> Message:

    message = Message(chat_id=chat_id, text=text)
    message.full_clean()
    message.save()

    return message


def chat_delete(
    chat: Chat,
) -> None:

    chat.delete()

    return None
