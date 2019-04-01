from django.db import models

# Create your models here.

class sensors(models.Model):
    temperature = models.FloatField(max_length=250);
    moisture = models.FloatField(max_length=250);
    humidity = models.FloatField(max_length=250);
    date = models.DateTimeField(auto_now=True);
    camera = models.ImageField(default='default.png', blank=True);
