from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Curso)
admin.site.register(CursoEstudiantes)
admin.site.register(Estudiante)
admin.site.register(Profesor)

class ProductoCategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('categoria_id', 'nombre', 'talle', 'cantidad', 'precio', 'fecha_actualizacion')
    list_display_links = ('nombre',)
    search_fields = ('nombre',)
    ordering = ('categoria_id', 'nombre')
    list_filter = ('categoria_id',)
    date_hierarchy = ('fecha_actualizacion')
    
admin.site.register(ProductoCategoria, ProductoCategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)