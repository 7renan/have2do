from django.shortcuts import redirect
from django.contrib import admin
from django.urls import path, include


def redirect_home(request):
    return redirect('projects:project_list')


urlpatterns = [
    path('', redirect_home),
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls', namespace='tasks')),
    path('projects/', include('projects.urls', namespace='projects')),
]

