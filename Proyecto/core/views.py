from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
    FormView,
)
from .forms import *
from .models import *

def index(request):
    return render(request, "core/index.html")



def indexproducto(request):
    return render(request, "core/indexproducto.html")

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'core/login.html'

class Register(FormView):
    template_name = 'core/register.html'
    form_class = CustomUserCreationForm
    redirect_autheticated_user = True
    success_url = reverse_lazy('core:index')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Register, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        return super(Register, self).get(*args, **kwargs)

#-----------------------------------------------------------------

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
    
class ProductoDetailTops(DetailView):
    model = Producto
    context_object_name = 'tops'
    template_name = 'core/producto_detail_tops.html'
    
class ProductoDeleteTops(DeleteView):
    model = Producto
    context_object_name = 'tops'
    success_url = reverse_lazy("core:producto_list_tops")
    template_name = 'core/producto_delete_tops.html'

#-----------------------------------------------------------------

class ProductoListJeans(ListView):
    model = Producto
    context_object_name = "jeans"
    queryset = Producto.objects.filter(categoria_id=2)
    template_name = "core/producto_list_jeans.html"
    
class ProductoUpdateJeans(UpdateView):
    model = Producto
    context_object_name = "jeans"
    form_class = ProductoForm
    success_url = reverse_lazy("core:producto_list_jeans")
    template_name = "core/producto_jeans_form.html"
    
class ProductoDetailJeans(DetailView):
    model = Producto
    context_object_name = 'jeans'
    template_name = 'core/producto_detail_jeans.html'
    
class ProductoDeleteJeans(DeleteView):
    model = Producto
    context_object_name = 'jeans'
    success_url = reverse_lazy("core:producto_list_jeans")
    template_name = 'core/producto_delete_jeans.html'
    


#-----------------------------------------------------------------

class ProductoListVestidos(ListView):
    model = Producto
    context_object_name = "vestidos"
    queryset = Producto.objects.filter(categoria_id=3)
    template_name = "core/producto_list_vestidos.html"

class ProductoUpdateVestidos(UpdateView):
    model = Producto
    context_object_name = "vestidos"
    form_class = ProductoForm
    success_url = reverse_lazy("core:producto_list_vestidos")
    template_name = "core/producto_vestidos_form.html"
    
class ProductoDetailVestidos(DetailView):
    model = Producto
    context_object_name = 'vestidos'
    template_name = 'core/producto_detail_vestidos.html'
    
class ProductoDeleteVestidos(DeleteView):
    model = Producto
    context_object_name = 'vestidos'
    success_url = reverse_lazy("core:producto_list_vestidos")
    template_name = 'core/producto_delete_vestidos.html'
    
    
