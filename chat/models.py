from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Chat(models.Model):
    Chat_name = models.CharField(max_length=50)


class Chat_Acc(models.Model):
    Acc_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Chat_id = models.ForeignKey(Chat, on_delete=models.CASCADE)


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    msg = models.CharField(max_length=50)
    Acc_sent = models.ForeignKey(User, on_delete=models.CASCADE)
    get_time = models.DateTimeField()

# class Room_Chat(models.Model):
#     name = models.CharField(max_length=20)

# class Room_Member(models.Model):
#     Room_ID = models.ForeignKey(Room_Chat, on_delete=models.CASCADE)
#     Acc_ID = models.ForeignKey(User, on_delete=models.CASCADE)