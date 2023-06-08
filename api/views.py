
from django.http import JsonResponse
from django.views import View
from .models import company

# Create your views here.

class companiaView(View):
    """ Esta clase es la que vamos a convertir nosotros en una vista 
        que sea capaz de procesar las respuestas"""
    
    def get(self, request):
        valor = list(company.objects.values())
        if len(valor)>0:
            datos = { 'mensajee' : "Exitoso" , "valor":valor}
        else:
            datos = { 'mensajee' : "compañia no encontrada"}
        return JsonResponse(datos)

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass