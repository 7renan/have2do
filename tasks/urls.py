from django.urls import path
from .views import task_list, task_create, task_delete, task_update

app_name = 'tasks'

urlpatterns = [
     path('list/', task_list, name='task_list'),
     path('create/', task_create, name='task_create'),
     path('delete/<int:pk_task>/', task_delete, name='task_delete'),
     path('update/<int:pk_task>/', task_update, name='task_update'),
]

