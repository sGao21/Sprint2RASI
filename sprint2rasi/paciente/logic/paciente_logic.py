from ..models import Paciente

def get_pacientes():
    pacientes= Paciente.objects.all()
    return pacientes