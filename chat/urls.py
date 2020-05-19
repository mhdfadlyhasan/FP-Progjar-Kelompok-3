from django.urls import path

from . import views


urlpatterns = [
    # ex: /chat/
    path('', views.room_list, name='home'), #main page chat langsung mengeluarkan list chat!
    # ex: /chat/1/
    #path('<int:Acc_id>/', views.room_list, name='room_list'),
    # ex: /chat/room_id/
    path('chat/<int:Chat_id>/', views.message_list, name='message_list'),
]