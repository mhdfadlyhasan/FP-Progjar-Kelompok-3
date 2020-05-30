from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Rename nama Room dan Room_Acc

class Room(models.Model):
    RoomName = models.CharField(max_length=50)

class Room_Acc(models.Model):
    AccID = models.ForeignKey(User, on_delete=models.CASCADE)
    # AccID = models.IntegerField() #dummy ID save
    RoomID = models.ForeignKey(Room, on_delete=models.CASCADE)


class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    msg = models.CharField(max_length=50)
    AccSent = models.ForeignKey(User, on_delete=models.CASCADE)
    # AccSent = models.IntegerField() #dummy ID sender
    getTime = models.DateTimeField()

