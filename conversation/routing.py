# conversation\routing.py
from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/conversation/<uuid:conversation_id>/', consumers.ConversationConsumer.as_asgi()),
]