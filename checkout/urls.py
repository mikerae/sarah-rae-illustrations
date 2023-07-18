from django.urls import path
from . import views
from checkout.webhooks.webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<ordder_number>',
         views.checkout_success, name='checkout_success'),
    path('webhook/', webhook, name='webhook'),
]
