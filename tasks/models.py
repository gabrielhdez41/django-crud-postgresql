from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'

    def __str__(self):
        return str(self.id)+"- "+self.title