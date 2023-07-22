""" Handles webhooks from stripe

    NB: Because the new stripe Payment Element was used rather than the Card
    Element. The Payment Element captured all the necessary user data, but then
    imediately passed a payment_succeded call to stripe. t was not properly
    understood how to input data to the payment intent before passing it to the
    Payment Element, the webhook paymentIntent received from stipe does not
    have all the required metadata to make order processing effective here.
"""
from django.http import HttpResponse


class StripeWhHandler():
    """ Handle Stripe webhooks """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = intent = event.data.object
        print(f'Successful PaymentIntent webhook reveived: {intent}')

        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database', status=200)  # noqa E501

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
