from django.db import models

# Create your models here.
from django.db import models

class Coin(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=20, decimal_places=8)
    market_cap = models.BigIntegerField()
    price_change_24h = models.FloatField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.symbol.upper()})"
