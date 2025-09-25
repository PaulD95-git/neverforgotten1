from django.core.mail import EmailMultiAlternatives, send_mail
from django.template.loader import render_to_string
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
from django.utils.html import strip_tags

from .models import Subscriber


def send_welcome_email(subscriber, request):
    """
    Send a welcome email to new subscribers.

    Args:
        subscriber: Subscriber object to welcome
        request: HttpRequest object for building absolute URLs

    Returns:
        None
    """
    unsubscribe_url = request.build_absolute_uri(
        reverse('newsletter:unsubscribe', args=[subscriber.email])
    )

    context = {
        'subscriber': subscriber,
        'unsubscribe_url': unsubscribe_url,
        'welcome_message': "Thank you for joining our community!",
        'features': [
            "New memorial features",
            "Community stories",
            "Special announcements"
        ]
    }

    subject = "Welcome to NeverForgotten!"
    html_content = render_to_string(
        'newsletter/emails/welcome_email.html',
        context
    )
    text_content = strip_tags(html_content)

    send_mail(
        subject=subject,
        message=text_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[subscriber.email],
        html_message=html_content,
        fail_silently=False
    )