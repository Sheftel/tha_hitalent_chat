from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import ChatCreateView, ChatDetailView, MessageCreateView

urlpatterns = format_suffix_patterns([
    path('', ChatCreateView.as_view(), name='chat_create'),
    path('<int:chat_id>/', ChatDetailView.as_view(), name='chat_detail'),
    path('<int:chat_id>/messages/', MessageCreateView.as_view(), name='message_create'),
])