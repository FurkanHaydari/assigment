from django.contrib.auth import get_user_model
from celery import shared_task
from django.core.mail import send_mail
from proje import settings
import json


@shared_task(bind=True)
def send_mail_to_users(self, trips):
    users = get_user_model().objects.all()
    content = 'This e-mail has been sent to inform users about the trips in the database.\n\n'
    for trip in trips:
        totalDistance = trip['totalDistance']
        startTime = trip['startTime']
        status = trip['status']
        passengerID = trip['passenger']
        sentence = 'passengerID: %s \n start Time: %s \n total distance: %s \n status:%s \n' % (
            passengerID, startTime, totalDistance, status)
        content = content + '\n' + sentence
    for user in users:
        subject = 'Hi From Celery!'
        message = content
        to_email = user.email

        send_mail(subject, message, settings.EMAIL_HOST_USER, [to_email])
    return "Done"
