from django.db import models

# Create your models here.

class sensors(models.Model):
    temperature = models.FloatField(max_length=250);
    moisture = models.FloatField(max_length=250);
    humidity = models.FloatField(max_length=250);
    fanStatus = models.TextField(max_length=250, default="Deactivated");
    lightStatus = models.TextField(max_length=250, default="Deactivated");
    action = models.TextField(max_length=250, default="None");
    date = models.DateTimeField(auto_now=True);
    camera = models.ImageField(default='default.png', blank=True);
