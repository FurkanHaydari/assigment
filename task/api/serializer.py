from djoser.serializers import UserSerializer, UserCreateSerializer
from rest_framework import serializers
from .models import Passenger, Trip, User


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = '__all__'


class UserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = User
        fields = '__all__'


class tripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'


class passengerSerializer(serializers.ModelSerializer):

    geziler = tripSerializer(many=True, read_only=True)

    class Meta:
        model = Passenger
        fields = '__all__'

# class passengerSerializer(serializers.ModelSerializer):

#     geziler = tripSerializer(many=True, read_only=True)

#     class Meta:
#         model = Passenger
#         fields = '__all__'
