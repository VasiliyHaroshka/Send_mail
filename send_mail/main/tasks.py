from django.core.mail import send_mail

from send_mail.celery import app
from .models import Contact
from .passwords import MY_EMAIL

from .service import send


@app.task
def send_spam(user_email):
    send(user_email)


@app.task
def send_beat_spam():
    for contact in Contact.objects.all():
        send_mail(
            'Вы подписаны на рассылку',
            'Получите письмо каждые 5 минут.',
            MY_EMAIL,
            [contact.email],
            fail_silently=False,
        )
