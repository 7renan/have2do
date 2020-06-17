from django.shortcuts import render, redirect
from .models import Task

tasks = []

def task_list(request):
    context = {
        'tasks': tasks,
    }
    return render(request, 'task_list.html', context)
    
    
def task_create(request):
    
    if request.method == 'POST':
        task = Task(
            request.POST['title'],
            request.POST['content'],
            request.POST['cover'],
        )

        tasks.append(task)
        return redirect('tasks:task_list')
    return render(request, 'task_create.html')
