from django.db import models


# Create your models here.

class Candle(models.Model):
    OPEN = models.FloatField()
    HIGH = models.FloatField()
    LOW = models.FloatField()
    CLOSE = models.FloatField()
    DATE = models.DateField()
    