from django.urls import path
from . import views
from checkout.webhooks.webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout/checkout_success/',
         views.checkout_success, name='checkout_success'),
    path('webhook/', webhook, name='webhook'),
    path('create_payment_intent/',
         views.create_payment_intent, name='create_payment_intent'),
]
