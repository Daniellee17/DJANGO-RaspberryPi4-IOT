from django.shortcuts import render
from django.http import HttpResponse
from .models import sensors
#----------------CAMERA----------------
import pygame, sys
from pygame.locals import *
import pygame.camera


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
    pygame.init()
    pygame.camera.init()
    cam = pygame.camera.Camera("/dev/video0",(352,288))
    cam.start()
    image= cam.get_image()
    pygame.image.save(image,'/home/pi/thesis/blinkled/assets/101.bmp')
    cam.stop()
    sensors.objects.filter(pk=12).update(camera="101.bmp")
    currentTemp = sensors.objects.only('temperature').get(pk=12).temperature
    currentHumidity = sensors.objects.only('humidity').get(pk=12).humidity

    if(currentTemp>30):
        print("(Pin 20) The fan is ON")
        GPIO.output(20, GPIO.HIGH)
        sensors.objects.filter(pk=12).update(fanStatus="Activated")
        if(currentHumidity<40):
            sensors.objects.filter(pk=12).update(action="Temperature too high, Humidity is too low!")
        else:
            sensors.objects.filter(pk=12).update(action="Temperature is too hot!")
    
    if(currentHumidity<40):
        if(currentTemp>30):
            print("(Pin 20) The fan is ON")
            GPIO.output(20, GPIO.HIGH)
            sensors.objects.filter(pk=12).update(fanStatus="Activated")
            sensors.objects.filter(pk=12).update(action="Temperature too high, Humidity is too low!")
        else:
            sensors.objects.filter(pk=12).update(action="Humidity is too low!")
    
    if(currentTemp<30):
        print("(Pin 20) The fan is OFF")
        GPIO.output(20, GPIO.LOW)
        sensors.objects.filter(pk=12).update(fanStatus="Deactivated")
        if(currentHumidity>40):
            sensors.objects.filter(pk=12).update(action="Normal")


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
        sensors.objects.filter(pk=12).update(lightStatus="Activated")


    if (request.GET.get('offLED_btn')):
        print("(Pin 21) The light is OFF")
        GPIO.output(21, GPIO.HIGH)
        sensors.objects.filter(pk=12).update(lightStatus="Deactivated")


    if (request.GET.get('onFAN_btn')):
        print("(Pin 20) The fan is ON")
        GPIO.output(20, GPIO.HIGH)
        sensors.objects.filter(pk=12).update(fanStatus="Activated")


    if (request.GET.get('offFAN_btn')):
        print("(Pin 20) The fan is OFF")
        GPIO.output(20, GPIO.LOW)
        sensors.objects.filter(pk=12).update(fanStatus="Deactivated")


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
