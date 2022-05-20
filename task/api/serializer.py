from asyncio.windows_events import NULL
from django.db.models import fields
from rest_framework import serializers
from .models import Passenger, Trip


class tripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'


class passengerSerializer(serializers.ModelSerializer):

    geziler = tripSerializer(many=True, read_only=True)

    class Meta:
        model = Passenger
        fields = '__all__'
