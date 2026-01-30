from django.http import Http404

from rest_framework.views import APIView
from rest_framework import serializers, status
from rest_framework.response import Response

from chat.models.chat import  Chat
from chat.selectors import chat_retrieve
from chat.services import chat_create, message_create, chat_delete
from chat.serializers import MessageSerializer


class ChatCreateView(APIView):
    class InputSerializer(serializers.Serializer):
        title = serializers.CharField()
    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Chat
            depth = 1
            fields = '__all__'


    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        chat = chat_create(**serializer.validated_data)
        data = self.OutputSerializer(chat).data

        return Response(data, status=status.HTTP_201_CREATED)


class ChatDetailView(APIView):
    class OutputSerializer(serializers.ModelSerializer):
        messages = serializers.SerializerMethodField()
        class Meta:
            model = Chat
            fields = '__all__'

        def get_messages(self, chat):
            limit = self.context.get('limit')
            messages = chat.messages.order_by("-created_at").all()[:limit]
            MessageSerializer(messages, many=True)
            return MessageSerializer(messages, many=True).data


    def get(self, request, chat_id):
        limit = request.query_params.get('limit', 20)
        limit = int(limit) if limit.isdigit() else 20
        limit = 100 if limit > 100 else limit

        chat = chat_retrieve(chat_id)
        if chat is None:
            raise Http404


        data = self.OutputSerializer(chat, context={'limit':limit}).data

        return Response(data)

    def delete(self, request, chat_id):
        chat = chat_retrieve(chat_id)

        if chat is None:
            raise Http404

        chat_delete(chat)

        return Response(status.HTTP_204_NO_CONTENT)


class MessageCreateView(APIView):
    class InputSerializer(serializers.Serializer):
        text = serializers.CharField()
    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        text = serializers.CharField()
        created_at = serializers.DateTimeField()

    def post(self, request, chat_id):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        chat = chat_retrieve(chat_id)

        if chat is None:
            raise Http404

        message = message_create(chat_id=chat_id, **serializer.validated_data)
        data = self.OutputSerializer(message).data

        return Response(data, status=status.HTTP_201_CREATED)


