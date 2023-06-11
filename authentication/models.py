from django.db import models
import uuid


# Create your models here.


class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    profile = models.CharField(max_length=255)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Driver(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    personalAddress = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    numberingPlate = models.CharField(max_length=255)
    vehicleImage = models.CharField(max_length=255)
    gender = models.IntegerField()
    state = models.IntegerField()
    type = models.IntegerField()
    status = models.IntegerField()
    active = models.BooleanField(default=False)
    subscribe = models.BooleanField(default=False)
    rating = models.FloatField(default=0)
    subscribeDate = models.CharField(max_length=255)
    subscribePath = models.CharField(max_length=255)
    pathSubscribe = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    isAvailable = models.BooleanField()

    def __str__(self):
        return self.name

