from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, serializers
from rest_framework.response import Response
from .serializer import tripSerializer, passengerSerializer
from .models import Passenger, Trip
from .tasks import send_mail_to_users


@api_view(['GET'])
def send_mail_to_all(request):
    items = Trip.objects.all()
    data = tripSerializer(items, many=True)
    send_mail_to_users.delay(data.data)
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def restricted(request, *args, **kwargs):
    return Response(data="TOKEN BAŞARILI ŞEKİLDE ÇALIŞIYOR", status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_passenger(request):
    item = passengerSerializer(data=request.data)

    if Passenger.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if item.is_valid():
        item.save()
        return Response(item.data, status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_trip(request):
    item = tripSerializer(data=request.data)

    if Trip.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_one_passenger(request, pk):

    items = Passenger.objects.get(pk=pk)

    if items:
        data = passengerSerializer(items)
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_one_trip(request, pk):

    items = Trip.objects.get(pk=pk)

    if items:
        data = tripSerializer(items)
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_passengers(request):

    if request.query_params:
        items = Passenger.objects.filter(**request.query_param.dict())
    else:
        items = Passenger.objects.all()

    if items:
        data = passengerSerializer(items, many=True)
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_trips(request):

    if request.query_params:
        items = Trip.objects.filter(**request.query_param.dict())
    else:
        items = Trip.objects.all()

    if items:
        data = tripSerializer(items, many=True)
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_passenger(request, pk):
    item = Passenger.objects.get(pk=pk)
    data = passengerSerializer(instance=item, data=request.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_trip(request, pk):
    item = Trip.objects.get(pk=pk)
    data = tripSerializer(instance=item, data=request.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_passenger(request, pk):
    item = Passenger.objects.get(pk=pk)
    if item:
        item.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_trip(request, pk):
    item = Trip.objects.get(pk=pk)
    if item:
        item.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
