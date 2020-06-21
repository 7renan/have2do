from django.shortcuts import render, redirect, get_object_or_404

# models
from .models import Task


def task_list(request):
    tasks = Task.objects.all()

    context = {
        'tasks': tasks,
    }

    return render(request, 'task_list.html', context)


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


def task_delete(request, pk_task):
    task = get_object_or_404(Task, pk=pk_task)
    task.delete()

    return redirect('tasks:task_list')