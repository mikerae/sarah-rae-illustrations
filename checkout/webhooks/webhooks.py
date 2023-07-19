"""
    copied from Stripe https://stripe.com/docs/webhooks/quickstart
    and modified for this project.
"""

import json
import stripe

from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from checkout.webhooks.webhook_handler import StripeWH_Handler


@require_POST
@csrf_exempt
def webhook():
    """ Listen for webhooks from stripe """

    # Set Up
    stripe.api_key = settings.STRIPE_SECRET_KEY
    webhook_secret = settings.STRIPE_APP_WEBHOOK_SIGNING_SECRET

    event = None
    payload = request.data

    try:
        event = json.loads(payload)
    except Exception as e:
        print('⚠️  Webhook error while parsing basic request.' + str(e))
        return JsonResponse(success=False)
    if webhook_secret:
        # Only verify the event if there is an endpoint secret defined
        # Otherwise use the basic event deserialized with json
        sig_header = request.headers.get('stripe-signature')
        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, webhook_secret
            )
        except stripe.error.SignatureVerificationError as e:
            print('⚠️  Webhook signature verification failed.' + str(e))
            return JsonResponse(success=False)

    # Set up a webhook handler instance
    handler - StripeWH_Handler(request)

    # Map webhook events to relevant handler functions
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed':
            handler.handle_payment_intent_payment_failed,

    }

    # Get the webhook events to relevant handler functions
    event_type = event['type']

    # If there is a handler for it, get it from the evnt map
    # Use the generic one by default
    event_handler = event_map.get(event_type, handler.handle_event)

    # Call the event handler with the event
    response = event_handler(event)
    return response

    # # Handle the event
    # if event and event['type'] == 'payment_intent.succeeded':
    #     # contains a stripe.PaymentIntent
    #     payment_intent = event['data']['object']
    #     # Then define and call a method to handle the
    #     # successful payment intent.
    #     # handle_payment_intent_succeeded(payment_intent)
    #     print('Payment for {} succeeded'.format(payment_intent['amount']))
    #     # Then define and call a method to handle the successful
    #     # attachment of a PaymentMethod.
    #     # handle_payment_method_attached(payment_method)
    # elif event['type'] == 'payment_method.attached':
    #     # contains astripe.PaymentMethod
    #     payment_method = event['data']['object']
    # else:
    #     # Unexpected event type
    #     print('Unhandled event type {}'.format(event['type']))

    # print('Webhook success!')
    # return JsonResponse(success=True)
