from ..models import Alergia

def get_alergias():
    alergias= Alergia.objects.all()
    return alergias