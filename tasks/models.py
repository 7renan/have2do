from django.db import models


class Task(models.Model):
    title = models.CharField('Título', max_length=50)
    description = models.TextField('Descrição')

    @property
    def resume(self):
        return self.description[:40]

    def __str__(self):
        return self.title
