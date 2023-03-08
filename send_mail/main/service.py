from django.core.mail import send_mail

from main.passwords import MY_EMAIL


def send(user_email):
    send_mail(
        'Вы подписаны на рассылку',
        'Получите письмо',
        MY_EMAIL,
        [user_email],
        fail_silently=False,
    )
