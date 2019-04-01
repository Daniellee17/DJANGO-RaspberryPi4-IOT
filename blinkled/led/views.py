from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def main(request):
    if (request.GET.get('onLED_btn')):
        print("The light is ON")

    if (request.GET.get('offLED_btn')):
        print("The light is OFF")

    if (request.GET.get('onFAN_btn')):
        print("The fan is ON")

    if (request.GET.get('offFAN_btn')):
        print("The fan is OFF")

    while True:
        return render(request, 'main.html')


def about(request):

    while True:
        return render(request, 'about.html')
