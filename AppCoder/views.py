from django.shortcuts import render, redirect
from AppCoder.models import Curso, Avatar, Profesores, Alumnos
from django.http import HttpResponse
from django.template import loader
from AppCoder.forms import Curso_formulario, UserEditForm, Profesores_formulario, Alumnos_formulario
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


def alta_curso(request, nombre):
    curso = Curso(nombre=nombre, camada=234511)
    curso.save()
    texto = f"Se guardo en la DB el curso: {curso.nombre} {curso.camada}"
    return HttpResponse(texto)

def inicio(request):
    avatar_url = None
    
    if request.user.is_authenticated:
        avatares = Avatar.objects.filter(user=request.user)
        if avatares.exists():
            avatar_url = avatares[0].imagen.url

    return render(request, "padre.html", {"avatar_url": avatar_url})    


def ver_curso(request):
    cursos = Curso.objects.all()
    avatar_url = None
    
    if request.user.is_authenticated:
        avatares = Avatar.objects.filter(user=request.user)
        if avatares.exists():
            avatar_url = avatares[0].imagen.url

    return render(request, "cursos.html", {"cursos": cursos, "avatar_url": avatar_url})



def alumnos(request):
    alumnos = Alumnos.objects.all()
    avatar_url = None

    if request.user.is_authenticated:
        avatares = Avatar.objects.filter(user=request.user)
        if avatares.exists():
            avatar_url = avatares[0].imagen.url

    return render(request, "alumnos.html", {"alumnos": alumnos, "avatar_url": avatar_url})


@login_required
def curso_formulario(request):
    if request.method == "POST":
        mi_formulario = Curso_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso = Curso(nombre=datos["nombre"], camada=datos["camada"])
            curso.save()
            return redirect('ver_curso')  # Redirige a la página donde se muestran todos los cursos

    return render(request, "formulario.html")


def buscar_curso(request):
    return render(request, "buscar_curso.html")


def buscar(request):

    if request.GET.get("nombre"):
        nombre = request.GET["nombre"]
        cursos = Curso.objects.filter(nombre__icontains=nombre)
        return render(request, "resultado_busqueda.html", {"cursos": cursos})
    else:
        return HttpResponse("Ingrese el nombre del curso")


@login_required
def elimina_curso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    cursos = Curso.objects.all()
    return render(request, "cursos.html", {"cursos": cursos})


@login_required
def editar(request, id):
    curso = Curso.objects.get(id=id)
    if request.method == "POST":
        mi_formulario = Curso_formulario(request.POST)

        if mi_formulario.is_valid():

            datos = mi_formulario.cleaned_data

            curso.nombre = datos["nombre"]

            curso.camada = datos["camada"]

            curso.save()

            cursos = Curso.objects.all()

            return render(request, "cursos.html", {"cursos": cursos})
    else:
        mi_formulario = Curso_formulario(initial={"nombre": curso.nombre, "camada": curso.camada})
    return render(request, "editar_curso.html", {"mi_formulario": mi_formulario, "curso": curso})

"""
def profesores(request):

    profes = Profesores.objects.all()

    return render(request, "profesores.html", {"profesores": profes})
    """

def profesores(request):
    profesores = Profesores.objects.all()
    avatar_url = None
    
    if request.user.is_authenticated:
        avatares = Avatar.objects.filter(user=request.user)
        if avatares.exists():
            avatar_url = avatares[0].imagen.url

    return render(request, "profesores.html", {"profesores": profesores, "avatar_url": avatar_url})    


def ver_profesores(request):
    profesores = Profesores.objects.all()
    dicc = {'profesores': profesores}
    plantilla = loader.get_template("profesores.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)


def profesores_formulario(request):
    if request.method == "POST":
        profesores = Profesores_formulario(request.POST)
        if profesores.is_valid():
            datos = profesores.cleaned_data
            profesores = Profesores(nombre=datos["nombre"], apellido=datos["apellido"], id_comision=datos["id_comision"])
            profesores.save()
            return redirect('ver_profesores.html')  # Redirige a la página deseada después de guardar los datos
    else:
        formulario = Profesores_formulario()
        return render(request, "profesores_formulario.html", {'formulario': formulario})


def buscar_profesores(request):

    return render(request, "buscar_profesores.html")


def buscarprofesores(request):

    if request.GET.get("nombre"):
        nombre = request.GET["nombre"]
        profesores = Profesores.objects.filter(nombre__icontains=nombre)
        return render(request, "resultado_busquedaprofesores.html", {"profesores": profesores})
    else:
        return HttpResponse("Ingrese el nombre del profesor")


def eliminar_profesores(request, id):
    profesores = Profesores.objects.get(id=id)
    profesores.delete()

    profesores = Profesores.objects.all()
    return render(request, "profesores.html", {"profesores": profesores})


def editar_profesores(request, id):
    profesores = Profesores.objects.get(id=id)
    if request.method == "POST":
        mi_formulario = Profesores_formulario(request.POST)

        if mi_formulario.is_valid():

            datos = mi_formulario.cleaned_data

            profesores.nombre = datos["nombre"]

            profesores.apellido = datos["apellido"]

            profesores.id_comision = datos["id_comision"]

            profesores.save()

            profesores = Profesores.objects.all()

            return render(request, "profesores.html", {"profesores": profesores})
    else:
        mi_formulario = Profesores_formulario(
            initial={"nombre": profesores.nombre, "apellido": profesores.apellido, "id_comision": profesores.id_comision})
    return render(request, "editar_profesores.html", {"mi_formulario": mi_formulario, "profesores": profesores})


def alumnos_formulario(request):
    if request.method == "POST":
        alumnos = Alumnos_formulario(request.POST)
        if alumnos.is_valid():
            datos = alumnos.cleaned_data
            alumnos = Alumnos(nombre=datos["nombre"], apellido=datos["apellido"], camada=datos["camada"])
            alumnos.save()
            return redirect('alumnos')  # Redirige al nombre de la URL definido en urls.py
    else:
        formulario = Alumnos_formulario()
        return render(request, "alumnos_formulario.html", {'formulario': formulario})


def buscar_alumnos(request):

    return render(request, "buscar_alumnos.html")


def buscaralumnos(request):
    if request.GET.get("nombre"):
        nombre = request.GET["nombre"]
        alumnos = Alumnos.objects.filter(nombre__icontains=nombre)
        return render(request, "resultado_busquedaalumnos.html", {"alumnos": alumnos})
    else:
        return HttpResponse("Ingrese el nombre del alumno")


@login_required
def eliminar_alumnos(request, id):
    alumnos = Alumnos.objects.get(id=id)
    alumnos.delete()

    alumnos = Alumnos.objects.all()
    return render(request, "alumnos.html", {"alumnos": alumnos})


@login_required
def editar_alumnos(request, id):
    alumnos = Alumnos.objects.get(id=id)
    if request.method == "POST":
        mi_formulario = Alumnos_formulario(request.POST)

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data

            alumnos.nombre = datos["nombre"]
            alumnos.apellido = datos["apellido"]
            alumnos.camada = datos["camada"]
            alumnos.save()

            alumnos = Alumnos.objects.all()

            return render(request, "alumnos.html", {"alumnos": alumnos})
    else:
        mi_formulario = Alumnos_formulario(initial={"nombre": alumnos.nombre, "apellido": alumnos.apellido, "camada": alumnos.camada})

    return render(request, "editar_alumnos.html", {"mi_formulario": mi_formulario, "alumnos": alumnos})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=contra)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirige al usuario a la página de inicio después del inicio de sesión exitoso
            else:
                return HttpResponse("Usuario no encontrado")
        else:
            return HttpResponse("Formato incorrecto")
    form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def register(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Usuario creado")

    else:
        form = UserCreationForm()
    return render(request, "registro.html", {"form": form})


def editarPerfil(request):
    usuario = request.user
    success_message = None

    if request.method == "POST":
        mi_formulario = UserEditForm(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            usuario.email = informacion["email"]
            password = informacion["password1"]
            usuario.set_password(password)
            usuario.save()
            success_message = "¡Perfil editado con éxito!"
        else:
            messages.error(request, "¡Hubo un error al editar el perfil! Por favor, corrige los errores.")
    else:
        mi_formulario = UserEditForm(initial={"email": usuario.email})

    return render(request, "editar_perfil.html", {"miFormulario": mi_formulario, "usuario": usuario, "success_message": success_message})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, "Has cerrado sesión exitosamente.")
        return redirect('home')

    return render(request, 'logout.html')
