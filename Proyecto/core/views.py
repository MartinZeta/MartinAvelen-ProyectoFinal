from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.

from . import forms, models


def index(request):
    return render(request, "core/index.html")


def profesor_list(request):
    consulta = models.Profesor.objects.all()
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
    consulta = models.Estudiante.objects.all()
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
    consulta = models.Curso.objects.all()
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



