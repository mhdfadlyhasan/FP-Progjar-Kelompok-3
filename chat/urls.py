from django.urls import path

from . import views


urlpatterns = [
    # ex: /chat/
    path('', views.login, name='login'),
    # ex: /chat/1/
    path('<int:Acc_id>/', views.room_list, name='room_list'),
    # ex: /chat/1/1/
    path('<int:Acc_id>/<int:Chat_id>/', views.message_list, name='message_list'),
]