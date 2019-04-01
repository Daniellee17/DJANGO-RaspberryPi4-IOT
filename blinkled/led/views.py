from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#!/usr/bin/python
import sys
import Adafruit_DHT
# Create your views here.
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
# LIGHT BULB
GPIO.setup(21, GPIO.OUT, initial=0)
# FAN
GPIO.setup(20, GPIO.OUT, initial=0)
sensor = Adafruit_DHT.DHT11


def main(request):
    if (request.GET.get('onLED_btn')):
        print("(Pin 21) The light is ON")
        GPIO.output(21, GPIO.HIGH)

    if (request.GET.get('offLED_btn')):
        print("(Pin 21) The light is OFF")
        GPIO.output(21, GPIO.LOW)

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

    while True:
        return render(request, 'main.html')


def about(request):

    while True:
        return render(request, 'about.html')
