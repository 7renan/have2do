from django.db import models

# models
from projects.models import Project


class Task(models.Model):
    title = models.CharField('Título', max_length=50)
    description = models.TextField('Descrição')
    project = models.ForeignKey(Project, verbose_name='Projeto', on_delete=models.CASCADE, blank=True, null=True)

    @property
    def resume(self):
        return self.description[:40]

    def __str__(self):
        return self.title
