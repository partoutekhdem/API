from rest_framework import serializers
from .models import *


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        def update(self, instance, validated_data):
            instance.nickname = validated_data.get('nickname', instance.nickname)
            instance.idCustomer = validated_data.get('idCustomer', instance.idCustomer)
            instance.profileCustomer = validated_data.get('profileCustomer', instance.profileCustomer)
            instance.nameCustomer = validated_data.get('nameCustomer', instance.nameCustomer)
            instance.phoneCustomer = validated_data.get('phoneCustomer', instance.phoneCustomer)
            instance.idDriver = validated_data.get('idDriver', instance.idDriver)
            instance.profileDriver = validated_data.get('profileDriver', instance.profileDriver)
            instance.nameDriver = validated_data.get('nameDriver', instance.nameDriver)
            instance.phoneDriver = validated_data.get('phoneDriver', instance.phoneDriver)
            instance.modelCar = validated_data.get('modelCar', instance.modelCar)
            instance.numberOfPassengers = validated_data.get('numberOfPassengers', instance.numberOfPassengers)
            instance.nameLocation = validated_data.get('nameLocation', instance.nameLocation)
            instance.nameDestinations = validated_data.get('nameDestinations', instance.nameDestinations)
            instance.status = validated_data.get('status', instance.status)
            instance.numberingPlate = validated_data.get('numberingPlate', instance.numberingPlate)
            instance.vehicleImage = validated_data.get('vehicleImage', instance.vehicleImage)
            instance.latitudeMyLocation = validated_data.get('latitudeMyLocation', instance.latitudeMyLocation)
            instance.longitudeMyLocation = validated_data.get('longitudeMyLocation', instance.longitudeMyLocation)
            instance.latitudeDestination = validated_data.get('latitudeDestination', instance.latitudeDestination)
            instance.longitudeDestination = validated_data.get('longitudeDestination', instance.longitudeDestination)
            instance.latitudeDriver = validated_data.get('latitudeDriver', instance.latitudeDriver)
            instance.longitudeDriver = validated_data.get('longitudeDriver', instance.longitudeDriver)
            instance.price = validated_data.get('price', instance.price)
            instance.ratingDriver = validated_data.get('ratingDriver', instance.ratingDriver)
            instance.typeCar = validated_data.get('typeCar', instance.typeCar)
            instance.minutes = validated_data.get('minutes', instance.minutes)
            instance.imagePayment = validated_data.get('imagePayment', instance.imagePayment)
            instance.save()
            return instance

class PrivacyPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivacyPolicy
        fields = '__all__'


class CallUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCall
        fields = '__all__'


class CallChauffeurSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChauffeurCall
        fields = '__all__'