from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponse
from .models import Message
from .models import Room_Acc
from django.template import loader

#untuk return menu awal chat, dulunya login

@login_required(login_url='/registration/')
def chat_home(request):
    return HttpResponse(str(request.user.id) + str(request.user.password))

# untuk return message list
@login_required(login_url='/registration/')
def message_list(request, Chat_id):
    msg_list = Message.objects.order_by('get_time').filter(chat=Chat_id)
    template = loader.get_template('chat/message_list.html')
    context = {
        'message_list': msg_list,
    }
    return HttpResponse(template.render(context, request))
    
#untuk return room list

@login_required(login_url='/registration/')
def room_list(request):
    chat_room_list = Room_Acc.objects.select_related().filter(AccID=request.user.id)
    template = loader.get_template('chat/room_list.html')
    context = {
        'chat_room_list': chat_room_list,
        'user_id':request.user.id,
    }
    print("requested room ")
    return HttpResponse(template.render(context, request))