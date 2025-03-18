from django.shortcuts import render
from django.http import HttpResponse


def ver_home(request):
    return render(request, 'home.html')


def ver_home2(request):
    return HttpResponse('Olá, mundo 2!')