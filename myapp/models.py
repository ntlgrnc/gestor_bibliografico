from django.db import models

# Create your models here.
class Users(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo = models.EmailField()
    clave = models.CharField(max_length=40)

    def __str__(self):
        return self.nombres + self.apellidos

class Introduction(models.Model):
    id_usuario = models.ForeignKey(Users, on_delete=models.CASCADE)
    citation = models.TextField()  
    article_title = models.CharField(max_length=255)
    topic = models.TextField()
    research_problem = models.TextField()
    research_objetive = models.TextField() 