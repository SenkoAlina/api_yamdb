import uuid
from django.core.mail import send_mail


def generate_confirmation_code():
    return uuid.uuid1()


def send_mail_to_user(email, confirmation_code):
    send_mail()
