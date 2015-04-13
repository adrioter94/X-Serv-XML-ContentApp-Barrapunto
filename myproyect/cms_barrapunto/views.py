from django.shortcuts import render
from models import Page
from django.http import HttpResponse, HttpResponseNotFound
from barrapunto import getNoticias

# Create your views here.


noticias = ""

def updateNoticias(request):
    global noticias 
    noticias = getNoticias()
    return HttpResponse('<br>Noticias actualizadas</br>')

def processCMS(request, recurso):
    if request.method == "GET":
        try:
            fila = Page.objects.get(name=recurso)
            return HttpResponse(fila.page + '<br><br>' + noticias)
        except Page.DoesNotExist:
            return HttpResponseNotFound('Page not found: /%s' % recurso)
    elif request.method == "PUT":
        try:
            cuerpo = request.body
            fila = Page.objects.create(name=recurso, page=cuerpo)
            fila.save()
            return HttpResponse("Nueva fila")
        except:
            return HttpResponseNotFound("Error")
