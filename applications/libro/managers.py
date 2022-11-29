from django.db import models

class LibroManager(models.Manager):
    def listar_libros(self, kword):
        resultado = self.filter(
            titulo__icontains=kword
        )
        return resultado

    def listar_libros2(self, kword, fecha, fecha2):
        resultado = self.filter(
            titulo__icontains=kword,
            fecha__range =  (fecha,fecha2)
        )
        return resultado
    def listar_libros_categoria(self, categoria):
        return self.filter(
            categoria__id=categoria
        ).order_by('titulo')

class CategoriaManager(models.Manager):
    def categoria_por_autor(self, autor):

        return self.filter(
            categoria_libro_autores__id=autor
        ).distinct()

