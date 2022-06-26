from django.http import HttpResponse
from django.template import Context, Template
from primerasvistas.models import familiar 

def creacion_tablas (request):
    mihtml=open(r"C:\Users\Alejo\Documents\django\casa\casa\plantilla\template2.html")
    plantilla= Template(mihtml.read())
    
       
    Familia = familiar (nombre="pablo", fecha_de_nacimiento=12/12/1932,edad=40)
    Familia.save()
    
    micontexto= Context({"Familia":Familia })
    documento=plantilla.render(micontexto)
    mihtml.close()
    return HttpResponse(documento)
    





