from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.http import HttpResponse
from django.db import IntegrityError
from django.contrib.auth.forms import UserCreationForm
from .models import Users, Introduction
import re, os

# Create your views here.
def index(request):
    introductions = Introduction.objects.all()
    return render(request,'index.html', {
        'introductions': introductions
    })

def signup(request):
    return render(request, 'registro.html', {
        'form': UserCreationForm
    })

def users(request):
    users = Users.objects.all()
    return render(request, 'usuarios.html', {
        'users': users
    })

def getUser(request, id):
    user = get_object_or_404(Users, id = id)
    return HttpResponse("Nombres usuario: %s " % user.nombres)

def createIntroduction(request):
    ruta_archivo = os.path.join(settings.BASE_DIR, 'myapp/static/archivos_txt', 'archivo.txt')
    contenido = "hola"
    if request.method == 'POST' and request.FILES.get('archivo'):
        archivo = request.FILES['archivo']
        # guardar el archivo en el servidor
        with open(ruta_archivo, 'wb+') as destino:
            for chunk in archivo.chunks():
                destino.write(chunk)

        # leer el contenido del archivo
        with open(ruta_archivo, 'r') as origen:
            contenido = origen.read()

            patron1 = r"generate a citation for this article\s*?\n\s*?PDF:\s*?(.+?)\s*?(?:Me:|$)"
            
            patron2 = r"what is the title of the article\?.*?PDF:\s*(.+?)\s*?(?:Me:|$)"

            patron3 = r"what is the topic of the article\?.*?PDF:\s*(.+?)\s*?(?:Me:|$)"

            patron4 = r"what is the research problem\?.*?PDF:\s*(.+?)\s*?(?:Me:|$)"

            patron5 = r"what is the objective of the research\?.*?PDF:\s*(.+?)\s*?(?:Me:|$)"

            citation = obtenerRespuesta(patron1, contenido)
            title = obtenerRespuesta(patron2, contenido)
            topic = obtenerRespuesta(patron3, contenido)
            problem = obtenerRespuesta(patron4, contenido)
            objetive = obtenerRespuesta(patron5, contenido)

            i = Introduction(
                citation = citation, 
                article_title = title,
                topic = topic,
                research_problem = problem,
                research_objetive = objetive,
                id_usuario = Users.objects.get(id=1))
            try:
                i.save()
                introductions = Introduction.objects.all()
                return render(request, 'index.html', {'introductions': introductions})
            except IntegrityError as e:
                print(f"Error al guardar el objeto: {e}")
            except Exception as e:
                # Capturar cualquier otra excepción
                print(f"Error desconocido al guardar el objeto: {e}")
            

def obtenerRespuesta(patron, contenido):
    match = re.search(patron, contenido, re.DOTALL)

    # Verificar si se encontró una coincidencia y extraer la respuesta
    if match:
        respuesta = match.group(1).strip()
        return respuesta
    else:
        return False

#Ejemplos
def ejemploconcatena(request, nombre):
    return HttpResponse("Hola %s , bienvenido/a" % nombre)

#def users(request):
#    users = list(Users.objects.values())
#    return JsonResponse(users, safe=False)

#def getUser(request, id):
#    user = get_object_or_404(Users, id = id)
#    return HttpResponse("Nombres usuario: %s " % user.nombres)