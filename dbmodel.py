from django.db import models

class Account:
    Acc_name = models.CharField(max_length=50)
	Acc_email = models.CharField(max_length=50)

class Chat:
    Chat_name = models.CharField(max_length=50)

class Message:
    chat_id int,
	msg = models.CharField(max_length=50)
	get_time = models.DateTimeField()
