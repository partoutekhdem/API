from rest_framework import serializers
from . import models


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.nickname = validated_data.get('nickname', instance.nickname)
        instance.code = validated_data.get('code', instance.code)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.profile = validated_data.get('profile', instance.profile)
        instance.save()
        return instance


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Driver
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.profile = validated_data.get('profile', instance.profile)
        instance.name = validated_data.get('name', instance.name)
        instance.nickname = validated_data.get('nickname', instance.nickname)
        instance.code = validated_data.get('code', instance.code)
        instance.phone = validated_data.get('phone', instance.phone)   
        instance.date = validated_data.get('date', instance.date)
        instance.department = validated_data.get('department', instance.department)
        instance.personalAddress = validated_data.get('personalAddress', instance.personalAddress)
        instance.model = validated_data.get('model', instance.model)
        instance.color = validated_data.get('color', instance.color)
        instance.numberingPlate = validated_data.get('numberingPlate', instance.numberingPlate)
        instance.vehicleImage = validated_data.get('vehicleImage', instance.vehicleImage)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.state = validated_data.get('state', instance.state)
        instance.type = validated_data.get('type', instance.type)
        instance.status = validated_data.get('status', instance.status)
        instance.active = validated_data.get('active', instance.active)
        instance.subscribe = validated_data.get('subscribe', instance.subscribe)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.subscribeDate = validated_data.get('subscribeDate', instance.subscribeDate)
        instance.subscribePath = validated_data.get('subscribePath', instance.subscribePath)
        instance.pathSubscribe = validated_data.get('pathSubscribe', instance.pathSubscribe)
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.longitude = validated_data.get('longitude', instance.longitude)
        instance.isAvailable = validated_data.get('isAvailable', instance.isAvailable)

        instance.save()
        return instance




