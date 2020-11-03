from django.contrib.auth.models import User
from rest_framework import serializers
from . import models


#Create serializer which will convert information about all users
class UserDataSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only = True)
    city = serializers.StringRelatedField(read_only = True)

    class Meta:
        model = models.UserData
        fields = ['user', 'city']


#Create serializer which will convert information about all cities
class CityDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Cities
        fields = ['name']


#Create serializer which will convert information about authorized users for djoser
class UserAuthSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["username", "email", "is_staff", ]


#Create serializer which will convert information about adverts
class AdvertsDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserAdverts
        fields = ['name', 'user', 'city', 'body', 'price']


#Create serializer which will convert information about filtered adverts
class AdvertsFilterDataSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    city = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = models.UserAdverts
        fields = ['name', 'user', 'city', 'body', 'price']