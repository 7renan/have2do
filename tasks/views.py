from django.shortcuts import render, redirect, get_object_or_404

# models
from .models import Task


# list
def task_list(request):
    tasks = Task.objects.all()

    context = {
        'tasks': tasks,
    }

    return render(request, 'task_list.html', context)


# create
def task_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']

        Task.objects.create(
            title=title,
            description=description
        )
        return redirect('tasks:task_list')
    return render(request, 'task_create.html')


# delete
def task_delete(request, pk_task):
    task = get_object_or_404(Task, pk=pk_task)
    task.delete()

    return redirect('tasks:task_list')


# update
def task_update(request, pk_task):
    task = Task.objects.get(pk=pk_task)
    context = {
        'task':task
    }

    if request.method == 'POST':
        new_title = request.POST['title']
        new_description = request.POST['description']
        task.title = new_title
        task.description = new_description
        task.save()
        return redirect('tasks:task_list')
    return render(request, 'task_update.html', context)