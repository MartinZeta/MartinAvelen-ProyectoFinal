from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
# Create your views here.

from .forms import *
from .models import *

def index(request):
    return render(request, "core/index.html")



def indexproducto(request):
    return render(request, "core/indexproducto.html")

class ProductoListTops(ListView):
    model = Producto
    context_object_name = "tops"
    queryset = Producto.objects.filter(categoria_id=1)
    template_name = "core/producto_list_tops.html"
    
class ProductoUpdateTops(UpdateView):
    model = Producto
    context_object_name = "tops"
    form_class = ProductoForm
    success_url = reverse_lazy("core:producto_list_tops")
    template_name = "core/producto_tops_form.html"
    
    
class ProductoListJeans(ListView):
    model = Producto
    context_object_name = "jeans"
    queryset = Producto.objects.filter(categoria_id=2)
    template_name = "core/producto_list_jeans.html"
    
    
class ProductoListVestidos(ListView):
    model = Producto
    context_object_name = "vestidos"
    queryset = Producto.objects.filter(categoria_id=3)
    template_name = "core/producto_list_vestidos.html"
