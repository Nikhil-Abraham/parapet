from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.security.websocket import AllowedHostsOriginValidator
from django.urls import path
import chatRoom.routing

application = ProtocolTypeRouter({
  'websocket': AuthMiddlewareStack(
      URLRouter(
        chatRoom.routing.websocket_urlpatterns
      ) 
    )
})