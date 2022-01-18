from django.shortcuts import render, redirect

from .models import Task
from .forms import TaskForm
from datetime import datetime


def index(request):
    form = TaskForm()
    tasks = Task.objects.all()
    context = {'tasks': tasks, 'task_form': form}
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'todolist/index.html', context)


def done_task(request, pk):
    task = Task.objects.get(id=pk)
    task.done = True
    task.done_time = datetime.utcnow()
    task.save()
    return redirect('index')


def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('index')
