from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import ChatCreateView, ChatDetailView, MessageCreateView

urlpatterns = format_suffix_patterns([
    path('', ChatCreateView.as_view(), name='chat_create'),
    path('<int:pk>', ChatDetailView.as_view(), name='chat_detail'),
    path('<int:pk>/messages/', MessageCreateView.as_view(), name='message_create'),
])