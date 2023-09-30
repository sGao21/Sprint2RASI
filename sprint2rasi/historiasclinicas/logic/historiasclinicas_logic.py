from ..models import HistoriaClinica

def get_historias():
    historias = HistoriaClinica.objects.all()
    return historias

def get_historia(id):
    historia = HistoriaClinica.objects.get(pk=id)
    return historia

def create_historia(form):
    historia = form.save()
    historia.save()
    return ()