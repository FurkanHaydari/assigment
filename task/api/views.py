from pickle import TRUE
from rest_framework import serializers
from rest_framework import status
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Passenger, Trip
from .serializer import passengerSerializer, tripSerializer


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'anasayfa': 'Hosgeldin'
    }

    return Response(api_urls)


@api_view(['POST'])
def add_passenger(request):
    item = passengerSerializer(data=request.data)

    # validating for already existing data
    if Passenger.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        print(item)
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add_trip(request):
    item = tripSerializer(data=request.data)

    # validating for already existing data
    if Trip.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        print(item)
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_passengers(request):

    # checking for the parameters from the URL
    if request.query_params:
        items = Passenger.objects.filter(**request.query_param.dict())
    else:
        items = Passenger.objects.all()

    # if there is something in items else raise error
    if items:
        data = passengerSerializer(items, many=True)
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_trips(request):

    # checking for the parameters from the URL
    if request.query_params:
        items = Trip.objects.filter(**request.query_param.dict())
    else:
        items = Trip.objects.all()

    # if there is something in items else raise error
    if items:
        data = tripSerializer(items, many=True)
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_items(request, pk):
    item = Passenger.objects.get(pk=pk)
    data = passengerSerializer(instance=item, data=request.data)
    print(data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_items(request, pk):
    item = Passenger.objects.get(pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['GET'])
def showAllModels(request):
    yolcu = Passenger.objects.all()
    gezi = Trip.objects.all()

    yolcuSerializer = passengerSerializer(yolcu, many=True)
    geziSerializer = tripSerializer(gezi, many=True)

    print(yolcuSerializer, geziSerializer)
    result = yolcuSerializer.data + geziSerializer.data

    return Response(result)
