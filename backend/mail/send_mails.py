"""Templates of mails to send."""
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.template.loader import render_to_string

User = get_user_model()


def send_mail_to_user(order) -> None:
    """Send mail to user."""
    html_content = render_to_string('cart_email_template.html', {
        'order': order,
    })

    send_mail(
        subject='Подтверждения заказа.',
        message='Ваша корзина.',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[f'{order.email}'],
        fail_silently=False,
        html_message=html_content
    )


def send_mail_to_restaurant(order) -> None:
    """Send mail to restaurant."""
    html_content = render_to_string('cart_email_template.html', {
        'name': order.first_name,
        'cart': order.cart,
        'total_price': order.total_price,
    })

    send_mail(
        subject='Подтверждения заказа.',
        message='Ваша корзина.',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[f'{order.email}'],
        fail_silently=False,
        html_message=html_content
    )
