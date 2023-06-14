from django.db import models

# Create your models here.
class Curso(models.Model):    #  herencia de Models para crear las bases de datos

    nombre = models.CharField(max_length=40)  # campo de tipo caracter (max= 40 caracters)

    camada = models.IntegerField()  # campo de tipo numero entero

 

class Estudiante(models.Model):

    nombre = models.CharField(max_length=30)

    apellido = models.CharField(max_length=30)
  
    email = models.EmailField()   # campo de tipo email

 

class Profesor(models.Model):

    nombre = models.CharField(max_length=30)

    apellido = models.CharField(max_length=30)

    email = models.EmailField()

    profesion = models.CharField(max_length=30)

 

class Entregable(models.Model):

    nombre = models.CharField(max_length=30)

    fechaDeEntrega = models.DateField()   # campo de tipo fecha

    entregada = models.BooleanField() # dato de tipo boolean