from django import forms

# models
from projects.models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        field = ['name', 'description', 'color']