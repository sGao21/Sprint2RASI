from ..models import Consulta

def get_consultas():
    consultas= Consulta.objects.all()
    return consultas