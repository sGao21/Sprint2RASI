from django.db import models

from historiasclinicas.models import HistoriaClinica

# Create your models here.
class Cirugia(models.Model):
    informacion = models.CharField(max_length=30)
    fecha= models.DateTimeField(null=False,default=None)
    historiasociada= models.ForeignKey(HistoriaClinica, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s' % (self.informacion, self.fecha, self.historiasociada)