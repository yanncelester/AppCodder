from django.db import models
from django.contrib.auth.models import User


# Create your models here.
#El modelo se comunica con la db y es como se va a estructurar la db 
#nosotros usamos SQL, entonces de este modo vamos a ver como se arman las tablas, todas las tablas tienen una primarykey que debe ser un id unico 

class Curso(models.Model): #estoy creando una clase curso que esta heredando la clase de model generando herencia de funcionalidades

    nombre = models.CharField(max_length=40) #campo char es str >> estoy definiendo tipo de dato de columna
    camada = models.IntegerField() #campo char es int >> estoy definiendo tipo de dato de columna

    def __str__(self): 
        return f"Nombre: {self.nombre} Camada: {self.camada}" #estoy armando como lo voy a ver en el admin

    class Meta:
        db_table = "AppCoder_curso"  # Especifica el nombre de la tabla en la base de datos

class Profesores(models.Model): #estoy creando una clase profesores 

    nombre = models.CharField(max_length=40) 
    apellido = models.CharField(max_length=40) 
    id_comision = models.IntegerField() 
    def __str__(self): 
        return f"Nombre: {self.nombre}   Apellido: {self.apellido}   id_comision: {self.id_comision}" #estoy armando como lo voy a ver en el admin

    class Meta:
        db_table = "AppCoder_profesores"  

class Alumnos(models.Model): #estoy creando una clase alumnos que esta heredando la clase de model generando herencia de funcionalidades

    nombre = models.CharField(max_length=40) #campo char es str >> estoy definiendo tipo de dato de columna
    apellido = models.CharField(max_length=40)
    camada = models.IntegerField() #campo char es int >> estoy definiendo tipo de dato de columna

    def __str__(self): 
        return f"Nombre: {self.nombre}  Apellido: {self.apellido}   Camada: {self.camada}" #estoy armando como lo voy a ver en el admin

    class Meta:
        db_table = "AppCoder_alumnos"  # Especifica el nombre de la tabla en la base de datos

class Avatar(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares" , null=True , blank=True)

    def __str__(self):
        return f"User: {self.user}  -  Imagen: {self.imagen}"        
