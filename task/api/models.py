from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(verbose_name='email',
                              max_length=255, unique=True)
    phone = models.CharField(null=True, max_length=255)
    REQUIRED_FIELDS = ['username', 'phone', 'first_name', 'last_name']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email


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
