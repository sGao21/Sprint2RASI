from ..models import HistoriaClinica

def get_historias():
    historias= HistoriaClinica.objects.all()
    return historias