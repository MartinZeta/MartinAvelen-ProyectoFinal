from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
# Create your views here.

from . import forms, models
from .models import *

def index(request):
    return render(request, "core/index.html")


def profesor_list(request):
    consulta = Profesor.objects.all()
    contexto = {"profesores": consulta}
    return render(request, "core/profesor_list.html", contexto)


def profesor_create(request):
    if request.method == "POST":
        form = forms.ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("core:profesor_list"))
    else:
        form = forms.ProfesorForm()
    return render(request, "core/profesor_create.html", {"form": form})

#-----------------------------------------------------------------

def estudiante_list(request):
    consulta = Estudiante.objects.all()
    contexto = {"estudiantes": consulta}
    return render(request, "core/estudiante_list.html", contexto)


def estudiante_create(request):
    if request.method == "POST":
        form = forms.EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("core:estudiante_list"))
    else:
        form = forms.EstudianteForm()
    return render(request, "core/estudiantes_create.html", {"form": form})


#----------------------------------------------------------------

def curso_list(request):
    consulta = Curso.objects.all()
    contexto = {"cursos": consulta}
    return render(request, "core/curso_list.html", contexto)

def curso_create(request):
    if request.method == "POST":
        form = forms.CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("core:curso_list"))
    else:
        form = forms.CursoForm()
    return render(request, "core/curso_create.html", {"form": form})



def indexproducto(request):
    return render(request, "core/indexproducto.html")

class ProductoListTops(ListView):
    model = Producto
    context_object_name = "object_list"
    template_name = "core/producto_list_tops.html"
