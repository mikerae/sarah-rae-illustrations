#! /usr/bin/env python3.6
# Python 3.6 or newer required.
# copied from Stripe https://stripe.com/docs/webhooks/quickstart
# and modified for this project

import json
import stripe

from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

# This is your test secret API key.
stripe.api_key = settings.STRIPE_SECRET_KEY

# Replace this endpoint secret with your endpoint's unique secret
# If you are testing with the CLI, find the secret by running 'stripe listen'
# If you are using an endpoint defined with the API or dashboard,
# look in your webhook settings
# at https://dashboard.stripe.com/webhooks
endpoint_secret = settings.STRIPE_WEBHOOK_SECRET_KEY


@require_POST
@csrf_exempt
def webhook():

    event = None
    payload = request.data

    try:
        event = json.loads(payload)
    except Exception as e:
        print('⚠️  Webhook error while parsing basic request.' + str(e))
        return JsonResponse(success=False)
    if endpoint_secret:
        # Only verify the event if there is an endpoint secret defined
        # Otherwise use the basic event deserialized with json
        sig_header = request.headers.get('stripe-signature')
        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, endpoint_secret
            )
        except stripe.error.SignatureVerificationError as e:
            print('⚠️  Webhook signature verification failed.' + str(e))
            return JsonResponse(success=False)

    # Handle the event
    if event and event['type'] == 'payment_intent.succeeded':
        # contains a stripe.PaymentIntent
        payment_intent = event['data']['object']
        # Then define and call a method to handle the
        # successful payment intent.
        # handle_payment_intent_succeeded(payment_intent)
        print('Payment for {} succeeded'.format(payment_intent['amount']))
        # Then define and call a method to handle the successful
        # attachment of a PaymentMethod.
        # handle_payment_method_attached(payment_method)
    elif event['type'] == 'payment_method.attached':
        # contains astripe.PaymentMethod
        payment_method = event['data']['object']

    else:
        # Unexpected event type
        print('Unhandled event type {}'.format(event['type']))

    return JsonResponse(success=True)
