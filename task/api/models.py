from django.db import models


class Passenger(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "api_passenger"


class Trip(models.Model):

    passenger = models.ForeignKey(
        Passenger, null=True, related_name='geziler', on_delete=models.CASCADE)
    totalDistance = models.CharField(max_length=255)
    startTime = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

    def __str__(self):
        return self.totalDistance

    class Meta:
        db_table = "api_trip"
