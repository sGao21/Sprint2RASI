from django.db import models

# Create your models here.
class Paciente(models.Model):
    nombre = models.CharField(max_length=20)
    cedula= models.IntegerField(null=False, default=None)
    edad= models.IntegerField(null=False, default=None)
    fechaNacimiento= models.DateField(null=False, default=None)

    def __str__(self):
        return '%s %s %s %s' % (self.nombre, self.cedula, self.edad , self.fechaNacimiento)