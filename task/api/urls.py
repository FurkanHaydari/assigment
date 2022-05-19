from . import views
from django.urls import path

urlpatterns = [
    path('', views.showAllModels, name='home'),
    path('createPassenger/', views.add_passenger, name='add-passenger'),
    path('createTrip/', views.add_trip, name='add-trip'),
    path('allPassengers/', views.view_passengers, name='view_items'),
    path('allTrips/', views.view_trips, name='view_items'),
    path('update/<int:pk>/', views.update_items, name='update-items'),
    path('item/<int:pk>/delete/', views.delete_items, name='delete-items'),
]
