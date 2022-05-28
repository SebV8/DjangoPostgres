from asyncio import tasks
from turtle import title
from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def list_task(request):
    tasks = Task.objects.all()
    return render(request,'list_task.html', {'tasks':tasks})

def create_task(request):
    tasksave = Task(title=request.POST['title'], description=request.POST['description'])
    tasksave.save()
    return redirect('/tasks/')

def delete_task(request, task_id):
    taskdelete=Task.objects.get(id=task_id)
    taskdelete.delete()
    return redirect('/tasks/')