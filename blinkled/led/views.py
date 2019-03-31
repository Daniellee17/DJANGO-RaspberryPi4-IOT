from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def main(request):
    if (request.GET.get('on_btn')):
        print("YOU HAVE TURNED IT ON")




    if (request.GET.get('off_btn')):
        print("YOU HAVE TURNED IT OFF")


    while True:
               return render(request,'main.html');
def about(request):

    while True:
               return render(request,'about.html');
