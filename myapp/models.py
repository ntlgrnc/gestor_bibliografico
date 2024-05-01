from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Users(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo = models.EmailField()
    clave = models.CharField(max_length=40)

    def __str__(self):
        return self.nombres + self.apellidos

class CargaAnalisis(models.Model):
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='id_usuario')
    citacion = models.TextField()
    tema = models.TextField()
    invest_problema = models.TextField()
    invest_objetivo = models.TextField() 
    ubicacion = models.CharField(max_length=255)
    titulo_articulo = models.TextField()
    resumen = models.TextField()
    problema = models.TextField()
    objetivos = models.TextField()
    referentes_teoricos = models.TextField()
    tipo_metodologia = models.CharField(max_length=100)
    diseno_metodologia = models.CharField(max_length=100)
    metodologia = models.TextField()
    resultados = models.TextField()
    conclusiones = models.TextField()
    lenguaje_texto = models.CharField(max_length=10)


class MensajesSoporte(models.Model):
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='id_usuario_origen')
    titulo_mensaje = models.CharField(max_length=255)
    cuerpo_mensaje = models.TextField()
    estado = models.CharField(max_length=100)
    adjuntos = models.ImageField(upload_to='myapp/static/imagenes_soporte/')