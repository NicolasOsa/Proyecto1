import datetime
from django.http import HttpResponse
from django.template import Template, Context, loader


def saludo(request):
    return HttpResponse("Hola Django equipo coder")

def segunda_vista(request):
    return HttpResponse("<br><br> <h1>Hola!</h1>")

def miNombreEs(request,nombre):
    data = f"Mi nombre es:<br><br>{nombre}"
    return HttpResponse(data)
    
def probandoTemplate(self):
    nombre ="Nicolas"
    apellido = "Osa"
    namelist = ["Gabriel", "Jimena", "Pedro", "Ignacio", "Natalia"]

    diccionario = {
        "nombre": nombre,
        "apellido": apellido,
        "namelist": namelist
    }

    #miHtml = open("C:/Users/osani/Desktop/Python/Django-proyecto1/Proyecto1/Proyecto1/plantillas/template1.html")
    #plantilla = Template(miHtml.read())
    #miHtml.close()
    #miContext = Context(diccionario)   # de esta manera damoscontexto al dict y lo podemos usar en la Template
    #documento = plantilla.render(miContext)
    
    plantilla = loader.get_template("template1.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)