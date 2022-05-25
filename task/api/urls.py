from . import views
from django.urls import path, include

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    # TOKEN DENEME FONKSİYONU
    path('authDeneme', views.restricted),
    # YOLCU OLUŞTUR
    path('createPassenger/', views.create_passenger, name='add-passenger'),
    # GEZİ OLUŞTUR
    path('createTrip/', views.create_trip, name='add-trip'),
    # TÜM YOLCULARI GÖRÜNTÜLE
    path('allPassengers/', views.view_passengers, name='view_passenger'),
    # TÜM GEZİLERİ GÖRÜNTÜLE
    path('allTrips/', views.view_trips, name='view_trip'),
    # TEK YOLCU GÖRÜNTÜLE
    path('passenger/<int:pk>/', views.get_one_passenger, name='get_one_passenger'),
    # TEK GEZİ GÖRÜNTÜLE
    path('trip/<int:pk>/', views.get_one_trip),
    # YOLCU GÜNCELLE
    path('updatePassenger/<int:pk>/',
         views.update_passenger, name='update-passenger'),
    # GEZİ GÜNCELLE
    path('updateTrip/<int:pk>/', views.update_trip, name='update-trip'),
    # YOLCU SİL
    path('passenger/<int:pk>/delete/',
         views.delete_passenger, name='delete-passenger'),
    # GEZİ SİL
    path('trip/<int:pk>/delete/', views.delete_trip, name='delete-trip'),

    path('sendmail/', views.send_mail_to_all),
]
