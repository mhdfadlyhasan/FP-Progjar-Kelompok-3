from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Rename nama Room dan Room_Acc
class Room(models.Model):
    Room_name = models.CharField(max_length=50)


class Room_Acc(models.Model):
    Acc_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Room_id = models.ForeignKey(Room, on_delete=models.CASCADE)


class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    msg = models.CharField(max_length=50)
    Acc_sent = models.ForeignKey(User, on_delete=models.CASCADE)
    get_time = models.DateTimeField()