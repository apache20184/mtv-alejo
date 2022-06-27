from django.http import HttpResponse
from django.template import Context, Template
from primerasvistas.models import familiar 

def creacion_tablas (request):
    mihtml=open(r"C:\Users\Alejo\Documents\django\casa\casa\plantilla\template2.html")
    plantilla= Template(mihtml.read())
    
       
    Familia = familiar (nombre="pablo", fecha_de_nacimiento="1932-05-09",edad="40")
    
    Familia.save()
    
    juan = familiar (nombre="juan", fecha_de_nacimiento="1978-09-12",edad="35")
    juan.save()
    
    julieta = familiar (nombre="julieta", fecha_de_nacimiento="1999-04-24",edad="78")
    julieta.save()
    micontexto= Context({"Familia":Familia, "juan":juan, "julieta":julieta})
    documento=plantilla.render(micontexto)
    mihtml.close()
    return HttpResponse(documento)
    





