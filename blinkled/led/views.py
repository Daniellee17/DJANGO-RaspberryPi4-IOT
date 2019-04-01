from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#!/usr/bin/python
import sys
import Adafruit_DHT
# Create your views here.
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT, initial=0)
GPIO.setup(19, GPIO.OUT, initial=0)
sensor = Adafruit_DHT.DHT11

def main(request):
    if (request.GET.get('on_btn')):
        print("YOU HAVE TURNED IT ON")
        GPIO.output(26, GPIO.HIGH)
        GPIO.output(19, GPIO.LOW)
        humidity, temperature = Adafruit_DHT.read_retry(sensor, 13)
        if humidity is not None and temperature is not None:
            print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
        else:
            print('Failed to get reading. Try again!')



    if (request.GET.get('off_btn')):
        print("YOU HAVE TURNED IT OFF")
        GPIO.output(26, GPIO.LOW)
        GPIO.output(19, GPIO.HIGH)


    while True:
               return render(request,'main.html');

def about(request):

    while True:
        return render(request, 'about.html')
