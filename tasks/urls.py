from django.urls import path
from .views import task_list, task_create

app_name = 'tasks'

urlpatterns = [
    path('list/', task_list, name='task_list'),
    path('create/', task_create, name='task_create'),
]

