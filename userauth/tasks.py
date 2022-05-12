from celery import shared_task

from django.core.mail import send_mail

from config import settings
from .models import UserAuth


@shared_task()
def send_email_to_all_user():
    users = UserAuth.objects.get(pk=2)
    mail_subject = 'Celery test'
    message = 'Hello man'
    to_email = users.email
    send_mail(
        subject=mail_subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[to_email],
        fail_silently=True,
    )

    return 'Send'
