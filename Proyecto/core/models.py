from django.db import models
from django.utils import timezone

class ProductoCategoria(models.Model):
    """Categoria de productos"""
    
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True, verbose_name = "descripción")
    
    def __str__(self):
        """Representa la instancia de la clase como una cadena de texto"""
        return self.nombre
    
    class Meta:
        verbose_name = "categoria de producto"
        verbose_name_plural = "categorias de productos"
 
class Producto(models.Model):
    categoria_id = models.ForeignKey(ProductoCategoria, null=True, blank=True, on_delete=models.SET_NULL)
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    talle = models.FloatField()
    cantidad = models.FloatField()
    descripcion = models.TextField(null=True, blank=True, verbose_name = "descripción")
    fecha_actualizacion = models.DateField(null=True, blank=True, default=timezone.now(), editable=False, verbose_name = "fecha de actualización")
    imagenProducto = models.ImageField(null=True, blank=True, upload_to="")
    
    def __str__(self):
        return f"{self.nombre} ({self.talle}) ${self.precio:.2f}"
    
    class meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"