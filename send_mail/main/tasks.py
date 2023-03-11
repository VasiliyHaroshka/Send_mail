from send_mail.celery import app

from .service import send


@app.task
def send_spam(user_email):
    send(user_email)
