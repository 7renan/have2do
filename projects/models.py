from django.db import models


class Project(models.Model):
    name = models.CharField('Nome', max_length=100)
    description = models.TextField('Descrição')
    color = models.CharField('Cor', max_length=7)

    @property
    def abstract(self):
        return self.description[:40]

    def __str__(self):
        return self.name

