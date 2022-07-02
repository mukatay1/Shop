from django.core.mail import send_mail

from celery import shared_task


@shared_task
def send_email():
    print(f'Отправляю письмо на почту')
    send_mail(
        'CandyShop',
        'Hello customer',
        'mr.mukatai@gmail.com',
        ['mr.mukatai@mail.ru'],
        fail_silently=False,
    )
