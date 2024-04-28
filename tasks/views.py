from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def registrar(request):
    djContext = dict()
    print(request.POST)
    if request.method == 'POST':
        task = Task(
            title = request.POST['titulo'],
            description = request.POST['descripcion']
        )
        task.save()
    tareas = Task.objects.all().order_by("-id")
    djContext["tareas"] = tareas
    return render(request, 'tasks/register.html', djContext)

def listar(request):
    djContext = dict()
    tareas = Task.objects.all().order_by("-id")
    djContext["tareas"] = tareas
    return render(request, 'tasks/list.html', djContext)

def eliminar(request, item_id):
    print("eric clapton")
    djContext = dict()
    if request.method == 'POST':
        tarea = Task.objects.get(pk=item_id)
        tarea.delete()
    return redirect("/tasks/")