from django.contrib import admin

# Register your models here.
from .models import Passenger
from .models import Trip

# Register your models here.
admin.site.register(Passenger)
admin.site.register(Trip)
