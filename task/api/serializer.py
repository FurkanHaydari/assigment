from django.db.models import fields
from rest_framework import serializers
from .models import Passenger, Trip


class tripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ('totalDistance', 'startTime', 'status')


class passengerSerializer(serializers.ModelSerializer):
    geziler = tripSerializer(many=True)

    class Meta:
        model = Passenger
        fields = ('name', 'geziler', 'email', 'status')
