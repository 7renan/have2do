from django.shortcuts import render, redirect, get_object_or_404

# models
from .models import Task

# forms
from .forms import TaskForm


# list
def task_list(request):
    tasks = Task.objects.all()
    form = TaskForm
    context = {
        'tasks': tasks,
        'form':form,
    }

    return render(request, 'task_list.html', context)


# create
def task_create(request):
    form = TaskForm(request.POST or None)
    context = {
        'form': form
    }

    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('tasks:task_list')
    return render(request, 'task_create.html', context)


# delete
def task_delete(request, pk_task):
    task = get_object_or_404(Task, pk=pk_task)
    task.delete()

    return redirect('tasks:task_list')


# update
def task_update(request, pk_task):
    task = Task.objects.get(pk=pk_task)
    form = TaskForm(request.POST or None, instance=task)
    context = {
        'task':task,
        'form': form,
    }

    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('tasks:task_list')
    return render(request, 'task_update.html', context)