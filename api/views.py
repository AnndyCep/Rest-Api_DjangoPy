
from typing import Any
from django import http
from django.http import JsonResponse
from django.views import View
from .models import company
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

class companiaView(View):
    """ Esta clase es la que vamos a convertir nosotros en una vista 
        que sea capaz de procesar las respuestas"""
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs) 
    """Metodo que se ejecuta en cada peticion (despachar o enviar)"""
    
    def get(self, request, id=0):
        if (id > 0):
            compania = list(company.objects.filter(id=id).values())
            if len(compania)>0:
                compañias = compania[0]
                datos =  { 'mensajee' : "Exitoso" , "compañias":compañias}
            else:
               datos = { 'mensajee' : "compañia no encontrada"} 
            return JsonResponse(datos)
        else:
            compania = list(company.objects.values())
            if len(compania)>0:
                datos = { 'mensajee' : "Exitoso" , "compania":compania}
            else:
                datos = { 'mensajee' : "compañia no encontrada"}
            return JsonResponse(datos)

    def post(self, request):
        jd = json.loads(request.body) # obtenemos la respuesta del body en formato json para guardarla en jd
        company.objects.create(nombre = jd['nombre'], sitioWeb =jd['sitioWeb'],fondacion= jd['fondacion']) 
        # Creamo a partir del modelo un nuevo elemento, como es un diccionario se realiza de la sigueitne forma. 
        datos = { 'mensajee' : "Exitoso"}
        return JsonResponse(datos)

    def put(self, request , id):
        jd = json.loads(request.body)
        compania = list(company.objects.filter(id=id).values())
        if len(compania)>0:
            conpañias =company.objects.get(id=id)
            conpañias.nombre = jd["nombre"]
            conpañias.sitioWeb = jd["sitioWeb"]
            conpañias.fondacion = jd["fondacion"]
            conpañias.save()
            datos = { 'mensajee' : "Exitoso"}
        else:
            datos = { 'mensajee' : "compañia no encontrada"}
        return JsonResponse(datos)
    
    def delete(self, request,id):
        compania = list(company.objects.filter(id=id).values())
        if len(compania)>0:
            conpañias =company.objects.get(id=id)
            conpañias.delete()
            datos = { 'mensajee' : "Exitoso"}
        else:
            datos = { 'mensajee' : "compañia no encontrada"}
        return JsonResponse(datos)