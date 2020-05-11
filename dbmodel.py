from django.db import models

class Account:
    Acc_name = models.CharField(max_length=50)
    Acc_email = models.CharField(max_length=50)

class Chat:
    Chat_name = models.CharField(max_length=50)
    accounts = models.ManyToManyField(Account)

class Message:
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    msg = models.CharField(max_length=50)
    get_time = models.DateTimeField()
