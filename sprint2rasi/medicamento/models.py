from django.db import models

from historiasclinicas.models import HistoriaClinica

# Create your models here.
class Medicamento(models.Model):
    nombre = models.CharField(max_length=20)
    historiasociada= models.ForeignKey(HistoriaClinica, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.nombre, self.historiasociada)