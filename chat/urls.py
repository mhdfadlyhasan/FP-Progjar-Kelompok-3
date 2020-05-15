from django.urls import path

from . import views


urlpatterns = [
    # ex: /polls/
    path('', views.login, name='login'),
    # ex: /polls/5/
    path('<int:Acc_id>/', views.room_list, name='room_list'),
    # ex: /polls/5/results/
    path('<int:Acc_id>/<int:Chat_id>/', views.message_list, name='message_list'),
]