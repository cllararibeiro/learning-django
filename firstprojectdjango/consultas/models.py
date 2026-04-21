from django.db import models

class Consulta(models.Model):
    paciente = models.CharField(max_length=100)
    data = models.DateTimeField()
    descricao = models.TextField()

    def __str__(self):
        return self.paciente
