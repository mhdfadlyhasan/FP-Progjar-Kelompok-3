from django.db import models


class Account:
    Acc_name = models.CharField(max_length=50)
    Acc_email = models.CharField(max_length=50)


class Chat:
    Chat_name = models.CharField(max_length=50)


class Chat_Acc:
    Acc_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    Chat_id = models.ForeignKey(Chat, on_delete=models.CASCADE)


class Message:
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    msg = models.CharField(max_length=50)
    Acc_sent = models.ForeignKey(Account, on_delete=models.CASCADE)
    get_time = models.DateTimeField()
