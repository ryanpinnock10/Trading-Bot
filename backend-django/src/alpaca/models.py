from django.db import models

# Create your models here.
class Positions(models.Model):
    symbol = models.CharField(),
    qty = models.IntegerField()

    def __str__(self):
        return self.symbol