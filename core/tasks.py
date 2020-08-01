
from celery import shared_task
from time import sleep
from django.core.mail import send_mail


@shared_task
def sleepy(duration):
    sleep(duration)
    return None


@shared_task
def send_email_task():
    sleep(5)
    send_mail('it worked', 'body', 'testmailofanoop2@gmail.com',
              ['testmailofanoop2@gmail.com'])
    return None
