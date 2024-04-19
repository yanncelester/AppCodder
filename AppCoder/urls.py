from django.urls import path
from django.urls import reverse
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("ver_curso", views.ver_curso, name="cursos"),  # Solo debe haber una entrada para ver_curso
    path("", views.inicio, name="home"),
    path("alumnos", views.alumnos , name="alumnos"),
    path("alta_curso", views.curso_formulario, name="alta_curso"),
    path("buscar_curso", views.buscar_curso, name="buscar_curso"),
    path("buscar", views.buscar),
    path("elimina_curso/<int:id>", views.elimina_curso, name="elimina_curso"),
    path("editar_curso/<int:id>", views.editar, name="editar_curso"),
    path("profesores", views.profesores, name="profesores"),
    path("ver_profesores", views.ver_profesores, name="ver_profesores"),
    path("alta_profesores", views.profesores_formulario),
    path("buscar_profesores.html", views.buscar_profesores),
    path("buscarprofesores", views.buscarprofesores),
    path("eliminar_profesores/<int:id>", views.eliminar_profesores, name="eliminar_profesores"),
    path("editar_profesores/<int:id>", views.editar_profesores, name="editar_profesores"),
    path("ver_alumnos.html", views.ver_alumnos, name="alumnos"),
    path("alta_alumnos", views.alumnos_formulario),
    path("buscar_alumnos.html", views.buscar_alumnos),
    path("buscaralumnos", views.buscaralumnos),
    path("eliminar_alumnos/<int:id>", views.eliminar_alumnos, name="eliminar_alumnos"),
    path("editar_alumnos/<int:id>", views.editar_alumnos, name="editar_alumnos"),
    path("login", views.login_request, name="Login"),
    path("register", views.register, name="Register"),
    path("logout/", LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("editarPerfil", views.editarPerfil, name="EditarPerfil")]