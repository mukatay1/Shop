from django.core.mail import send_mail

from celery import shared_task

from .models import Newsletter


@shared_task
def send_email():
    emails = Newsletter.objects.all()
    send_mail(
        'CandyShop',
        'Hello customer',
        'mr.mukatai@gmail.com',
        [f'{email}' for email in list(emails)],
        fail_silently=False,
    )
