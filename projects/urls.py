from django.urls import path

# views
from . import views

app_name = 'projects'

urlpatterns = [
    path('list/', views.project_list, name='project_list'),
]