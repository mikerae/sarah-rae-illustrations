from django.http import JsonResponse


class StripeWH_Handler():
    """ Handle Stripe webhooks """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return JsonResponse(
            content=f'Unhandled webhook received: {event["type"]}', status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle a payment_intent_succeeded webhook event
        """
        intent = event.data.objects
        print(intent)
        return JsonResponse(
            content=f'Webhook received: {event["type"]}',
            status=200,)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle a payment_intent_payment_failed webhook event
        """
        return JsonResponse(
            content=f'Webhook received {event["type"]}',
            status=200,)
