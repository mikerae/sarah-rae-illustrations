from django.urls import path
from . import views
from checkout.webhooks.webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/',
         views.checkout_success, name='checkout_success'),
    path('cache_checkout_data/', views.cache_checkout_data,
         name='cache_checkout_data'),
    path('webhook/', webhook, name='webhook'),
    path('create_payment_intent/',
         views.create_payment_intent, name='create_payment_intent'),
]
