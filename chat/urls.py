from django.urls import path
from .views import chat, room, send, getmessages

app_name = "chat"

urlpatterns = [
    path('', chat, name='chat'),
    path("room/<str:friend>",room,name='room'),
    path("send/",send,name='send'),
    path("getmessages/<str:friend>",getmessages,name='getmessages'),
]