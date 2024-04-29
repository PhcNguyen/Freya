from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def press(request):
    return HttpResponse('Hello')


def contact(request):
    return HttpResponse('0937.127.172')
