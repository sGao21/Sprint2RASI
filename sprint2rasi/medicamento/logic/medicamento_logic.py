from ..models import Medicamento

def get_medicamentos():
    medicamentos= Medicamento.objects.all()
    return medicamentos