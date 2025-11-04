from django.shortcuts import render

# Create your views here.
import requests
from django.shortcuts import render

def crypto_prices(request):
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd',
        'ids': 'bitcoin,ethereum,ripple,cardano,solana',
    }
    response = requests.get(url, params=params)
    data = response.json()
    return render(request, 'crypto/crypto.html', {'data': data})
