import datetime
from django.shortcuts import render
from django.views.generic import ListView
#modelos local
from .models import Libro



class listLibros(ListView):
    model = Libro
    template_name = "libro/lista.html"
    context_object_name = 'lista_libros'
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')
        palabra_clavefecha = self.request.GET.get("fecha",'')
        palabra_clavefecha2 = self.request.GET.get("fecha2",'')
        if palabra_clavefecha and palabra_clavefecha2:
            return Libro.objects.listar_libros2(palabra_clave, palabra_clavefecha, palabra_clavefecha2)
        else:
            return Libro.objects.listar_libros(palabra_clave)
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')
        palabra_clavefecha = self.request.GET.get("fecha",'')

