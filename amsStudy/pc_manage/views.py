from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def pcmindex(request):

    print('request.get_host():', request.get_host())

    return HttpResponse('Hello!')