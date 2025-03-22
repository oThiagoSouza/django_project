from django.shortcuts import render
from django.http import HttpResponse


def ver_home(request):
    if request.method == 'GET':
        return render(request, 'home.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        
        if nome != nome and senha != senha:
            HttpResponse('Usuário ou senha incorreto')
        else:
            return HttpResponse('Usuário e senha corretos')

def ver_home2(request):
    return HttpResponse('Olá, mundo 2!')