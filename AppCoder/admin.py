from django.contrib import admin
from .models import *

admin.site.register(Curso) #para que en nuestro admin esté registrado el modelo cursos

admin.site.register(Profesores) #para que en nuestro admin esté visible en el planel de admin 

admin.site.register(Alumnos) 


# Register your models here.
