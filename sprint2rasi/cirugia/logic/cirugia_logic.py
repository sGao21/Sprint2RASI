from ..models import Cirugia

def get_cirugias():
    cirugias= Cirugia.objects.all()
    return cirugias