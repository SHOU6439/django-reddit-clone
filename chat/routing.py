from django.urls import path

from .consumers import ChatConsumer

websocket_urlpatterns = [
    path(r'/ws/chat/dm/detail/<int:pk>', ChatConsumer.as_asgi()),
]