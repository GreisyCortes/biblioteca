from django.db import models
from django.db.models import Q

class AutorManager(models.Manager):
    """manager para el modelo autor"""

    def buscar_autor(self, kword):
        resultado = self.filter(
            nombre__icontains=kword
                                )
        return resultado

    def buscar_autor2(self, kword):#busca coincidencias de nombre y apellido
        resultado = self.filter(
            Q(nombre__icontains=kword) | Q(apellidos__icontains=kword)
        )

    def buscar_autor3(self, kword):#excluye a los que tengan edad de 25
        resultado = self.filter(
            Q(nombre__icontains=kword) | Q(apellidos__icontains=kword)
        ).exclude(edad=25)
        return resultado

    def buscar_autor4(self, kword):#busca a los que tenga mayor de edad 30
        resultado = self.filter(
            edad__gt=30,#mayor que 30 la coma es para indicar una funcion AND
            edad__lt=60#menor que 60
        )
        return resultado