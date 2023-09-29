from django.db import models

from paciente.models import Paciente

# Create your models here.
class HistoriaClinica(models.Model):
    anotacionjesimportantes = models.CharField(max_length=500)
    eps= models.CharField(max_length=20)
    rh=models.CharField(max_length=5)
    email=models.EmailField()
    pacienteasociado=models.OneToOneField(Paciente,on_delete=models.CASCADE,primary_key=True)

    def __str__(self):
        return '%s %s %s %s %s' % (self.anotacionesimportantes, self.eps, self.rh, self.email, self.pacienteasociado)