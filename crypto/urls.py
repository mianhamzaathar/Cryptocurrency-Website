from django.urls import path
from .views import crypto_prices

urlpatterns = [
    path('', crypto_prices, name='crypto-home'),
]
