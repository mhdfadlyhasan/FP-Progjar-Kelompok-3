from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Message
from .models import Chat
from django.template import loader

def login(request):
    return HttpResponse("ini menu login heheh")

def message_list(request, Chat_id,Acc_id):
    msg_list = Message.objects.order_by('get_time')
    template = loader.get_template('chat/message_list.html')
    context = {
        'message_list': msg_list,
    }
    return HttpResponse(template.render(context, request))

def room_list(request,Acc_id):
    chat_room_list = Chat.objects.order_by('Chat_name')
    template = loader.get_template('chat/room_list.html')
    context = {
        'chat_room_list': chat_room_list,
    }
    return HttpResponse(template.render(context, request))