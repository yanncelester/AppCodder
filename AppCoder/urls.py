from django.urls import path
from . import views


urlpatterns = [
    #path("alta_curso/<nombre>", views.alta_curso),
    path("ver_curso", views.ver_curso, name= "cursos"), #el name es el identificador para cuando estemos accediendo relativamente
    path("", views.inicio, name= "home"),
    path("alumnos", views.alumnos, name ="alumnos" ),
    path("alta_curso", views.curso_formulario),
    path("buscar_curso" , views.buscar_curso),
    path("buscar" , views.buscar),
    path("elimina_curso/<int:id>", views.elimina_curso, name="elimina_curso"),
    path("editar_curso/<int:id>" , views.editar , name= "editar_curso"),
    path("profesores", views.profesores, name ="profesores" ),
    path("ver_profesores", views.ver_profesores, name= "profesores"),
    path("alta_profesores", views.profesores_formulario),
    path('ver_profesores.html', views.ver_profesores, name='ver_profesores'),
    path("buscar_profesores.html" , views.buscar_profesores),
    path("buscarprofesores" , views.buscarprofesores),
    path("eliminar_profesores/<int:id>", views.eliminar_profesores, name="eliminar_profesores"),
    path("editar_profesores/<int:id>" , views.editar_profesores , name= "editar_profesores"),
    path("ver_alumnos.html", views.ver_alumnos, name="alumnos"),
    path("alta_alumnos", views.alumnos_formulario),
    path("buscar_alumnos.html" , views.buscar_alumnos),
    path("buscaralumnos" , views.buscaralumnos),
    path("eliminar_alumnos/<int:id>", views.eliminar_alumnos, name="eliminar_alumnos"),
    path("editar_alumnos/<int:id>" , views.editar_alumnos , name= "editar_alumnos")
]