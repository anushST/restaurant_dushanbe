"""Templates of mails to send."""
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

User = get_user_model()


def send_mail_to_user(user, code: str) -> None:
    """Send mail to user."""
    send_mail(
        subject='Подтверждения заказа.',
        message=f'Код: {code}',
        from_email='from@example.com',
        recipient_list=[f'{user.email}'],
        fail_silently=False,
    )
