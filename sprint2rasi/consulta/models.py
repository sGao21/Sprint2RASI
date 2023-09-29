from django.db import models

from historiasclinicas.models import HistoriaClinica

# Create your models here.
class Consulta(models.Model):
    fecha = models.DateTimeField(null=False,default=None)
    diagnostico= models.CharField(max_length=500)
    historiasociada= models.ForeignKey(HistoriaClinica, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s' % (self.fecha, self.diagnostico, self.historiasociada)