from django.shortcuts import render, redirect
from .models import Course

# Create your views here.


def index(request):
    return render(request, 'index.html')


def cursos(request):
    cursosListado = Course.objects.all()
    return render(request, 'cursos.html', {"curso": cursosListado})


def crear_curso(request):
    return render(request, 'crear_curso.html')


def carreras(request):
    return render(request, 'carreras.html')


def crear_carrera(request):
    return render(request, 'crear_carrera.html')


def eliminar_curso(idcourse):
    curso = Course.objects.get(idcourse=idcourse)
    curso.delete()
    return redirect('/cursos/')


def registrar_curso(request):
    code = request.POST['code']
    name = request.POST['name']
    hour = request.POST['hour']
    credits = request.POST['credits']
    state = request.POST['state']
    curso = Course.objects.create(
        code=code, name=name, hour=hour, credits=credits, state=state)
    return redirect('/crear_curso/')
