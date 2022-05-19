from django.db import models


class Passenger(models.Model):
    passenger_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=255)
    trips = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "api_passenger"


class Trip(models.Model):
    trip_id = models.AutoField(primary_key=True)
    passenger = models.ForeignKey(
        Passenger, related_name='geziler', on_delete=models.CASCADE)
    totalDistance = models.CharField(max_length=255)
    startTime = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.totalDistance

    class Meta:
        db_table = "api_trip"
