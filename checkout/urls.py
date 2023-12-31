""" Url definitions for checkout app"""
from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
     path('', views.checkout, name='checkout'),
     path('order_form_not_valid/',
          views.order_form_not_valid,
          name='order_form_not_valid'),
     path('checkout_success/',
          views.checkout_success,
          name='checkout_success'),
     path('webhook/', webhook, name='webhook'),
     path('create_payment_intent/',
          views.create_payment_intent,
          name='create_payment_intent'),
     path('save_userdata_checked/',
          views.save_userdata_checked,
          name='save_userdata_checked'),
]
