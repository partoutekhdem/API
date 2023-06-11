from django.db import models
import uuid



class Offer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_driver = models.CharField(max_length=255)
    profileDriver = models.CharField(max_length=255)
    nameDriver = models.CharField(max_length=255)
    phoneDriver = models.CharField(max_length=255)
    carModel = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    numberingPlate = models.CharField(max_length=255)
    vehicleImage = models.CharField(max_length=255)
    longitudeDriver = models.CharField(max_length=255)
    latitudeDriver =  models.CharField(max_length=255)
    price =  models.CharField(max_length=255)
    rating =  models.CharField(max_length=255)
    typeCar = models.CharField(max_length=255)
    minutes = models.CharField(max_length=255)


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    idCustomer = models.CharField(max_length=255)
    profileCustomer = models.CharField(max_length=255)
    nameCustomer = models.CharField(max_length=255)
    phoneCustomer = models.CharField(max_length=255)
    idDriver = models.CharField(max_length=255)
    profileDriver = models.CharField(max_length=255)
    nameDriver = models.CharField(max_length=255)
    phoneDriver = models.CharField(max_length=255)
    modelCar = models.CharField(max_length=255)
    numberOfPassengers = models.CharField(max_length=255)
    nameLocation = models.CharField(max_length=255)
    nameDestinations = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    numberingPlate = models.CharField(max_length=255)
    vehicleImage = models.CharField(max_length=255)
    latitudeMyLocation = models.CharField(max_length=255)
    longitudeMyLocation = models.CharField(max_length=255)
    latitudeDestination = models.CharField(max_length=255)
    longitudeDestination = models.CharField(max_length=255)
    latitudeDriver = models.CharField(max_length=255)
    longitudeDriver = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    ratingDriver = models.CharField(max_length=255)
    typeCar = models.CharField(max_length=255)
    minutes = models.CharField(max_length=255)
    offers=models.ManyToManyField(Offer, blank=True)
    imagePayment=models.CharField(max_length=255, default='')


class PrivacyPolicy(models.Model):
    privacyPolicyArabic = models.TextField()
    privacyPolicyEnglish = models.TextField()
    privacyPolicyFrench = models.TextField()


class UserCall(models.Model):
    id = models.AutoField
    content = models.CharField(max_length=255)
    number = models.IntegerField()
    active = models.BooleanField()


class ChauffeurCall(models.Model):
    id = models.AutoField
    content = models.CharField(max_length=255)
    number = models.IntegerField()
    active = models.BooleanField()
