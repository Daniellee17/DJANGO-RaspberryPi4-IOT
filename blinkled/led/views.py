from django.shortcuts import render
from django.http import HttpResponse
from .models import sensors


#!/usr/bin/python
import sys
import Adafruit_DHT
# Create your views here.
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
# LIGHT BULB
GPIO.setup(21, GPIO.OUT, initial=1)
# FAN
GPIO.setup(20, GPIO.OUT, initial=0)
# DHT11
sensor = Adafruit_DHT.DHT11
# SOIL MOISTURE SENSOR
GPIO.setup(12, GPIO.IN)


def main(request):
    print("------------------------------------------REFRESHED!------------------------------------------")
    values = sensors.objects.all()
    humidity, temperature = Adafruit_DHT.read_retry(sensor, 16)
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
    else:
        print('Failed to get reading. Try again!')

    print("(Pin 16 for DHT11) Page refreshed!")

    if GPIO.input(12):
        print("Water Detected!")
    else:
        print("No Water Detected!")

    sensors.objects.filter(pk=12).update(temperature=temperature, humidity=humidity, moisture = 1.0)

    if (request.GET.get('onLED_btn')):
        print("(Pin 21) The light is ON")
        GPIO.output(21, GPIO.LOW)

    if (request.GET.get('offLED_btn')):
        print("(Pin 21) The light is OFF")
        GPIO.output(21, GPIO.HIGH)

    if (request.GET.get('onFAN_btn')):
        print("(Pin 20) The fan is ON")
        GPIO.output(20, GPIO.HIGH)

    if (request.GET.get('offFAN_btn')):
        print("(Pin 20) The fan is OFF")
        GPIO.output(20, GPIO.LOW)

    if (request.GET.get('refresh_btn')):
        humidity, temperature = Adafruit_DHT.read_retry(sensor, 16)
        if humidity is not None and temperature is not None:
            print(
                'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
        else:
            print('Failed to get reading. Try again!')

        print("(Pin 16 for DHT11) Page refreshed!")

        if GPIO.input(12):
            print("Water Detected!")
        else:
            print("No Water Detected!")

        sensors.objects.filter(pk=12).update(temperature=temperature, humidity=humidity, moisture = 1.0)



    return render(request, 'main.html', {'values': values})



def about(request):

    while True:
        return render(request, 'about.html')
