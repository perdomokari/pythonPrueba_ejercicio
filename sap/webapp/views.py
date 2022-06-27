from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bienvenido(request):
    #return HttpResponse('Hola mundo desde Django')
    return render(request,'kariApp.html')


def despedida(request):
    return HttpResponse('Despedida desde Django')

