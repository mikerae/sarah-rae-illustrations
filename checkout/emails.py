""" Send an email """
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


def send_confirmation_email(intent, order):
    """ Send the user a confimation email """
    # intent = event.data.object
    cust_email = intent["receipt_email"]
    subject = render_to_string(
        'checkout/email_templates/confirmation_email_subject.txt',
        {'order': order}
    )
    body = render_to_string(
        'checkout/email_templates/confirmation_email_body.txt',
        {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL}
    )

    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [cust_email]
        )
    return
