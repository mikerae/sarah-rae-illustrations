"""
Stripe Endpoint copied from Strip docs,
and  modified for this project
"""
import json
import os
import stripe
from django.conf import settings

# from flask import Flask, render_template, jsonify, request


# This is your test secret API key.
# stripe_public_key = settings.STRIPE_PUBLIC_KEY
# print(stripe_public_key)

# app = Flask(__name__, static_folder='public',
#             static_url_path='', template_folder='public')


# def calculate_order_amount(items):
#     # Replace this constant with a calculation of the order's amount
#     # Calculate the order total on the server to prevent
#     # people from directly manipulating the amount on the client
#     return 1400


# @app.route('/create-payment-intent', methods=['POST'])
# def create_payment():
#     try:
#         data = json.loads(request.data)
#         # Create a PaymentIntent with the order amount and currency
#         intent = stripe.PaymentIntent.create(
#             amount=calculate_order_amount(data['items']),
#             currency='gbp',
#             automatic_payment_methods={
#                 'enabled': True,
#             },
#         )
#         return jsonify({
#             'clientSecret': intent['client_secret']
#         })
#     except Exception as e:
#         return jsonify(error=str(e)), 403
# if __name__ == '__main__':
#     app.run(port=4242)
