from django.shortcuts import render, redirect
from AppCoder.models import Curso, Avatar
from django.http import HttpResponse
from django.template import loader
from AppCoder.forms import Curso_formulario, UserEditForm
from django.http import Http404
from AppCoder.forms import Profesores_formulario  
from AppCoder.models import Profesores 
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from AppCoder.models import Alumnos
from AppCoder.forms import Alumnos_formulario 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm  #importamos de django traemos las clases para crear un nuevo usuario y para autenticarlo
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from .models import Avatar





# Create your views here.

def alta_curso(request, nombre):
    curso = Curso(nombre = nombre, camada =234511)
    curso.save()
    texto = f"Se guardo en la DB el curso: {curso.nombre} {curso.camada}"
    return HttpResponse(texto)


def inicio(request):
    return render(request, "padre.html") #cuando llega la petición voy a retornar un render, es decir a mostrar resultados
#render quiere decir mostrar, visualizar, cuando se genera el render se manda el resultado, generalmente porque pasan cosas como procesar datos, todo a nivel servisdor
#el request  es el pedido, el render es el response o sea la respuesta

def ver_curso(request):
        cursos = Curso.objects.all()
        print(cursos)  # Verifica si se están recuperando los cursos correctamente
        dicc = {'cursos': cursos}
        plantilla = loader.get_template("cursos.html")
        print(dicc)  # Verifica si los datos se están pasando correctamente a la plantilla
        documento = plantilla.render(dicc)
        return HttpResponse(documento)

        
def alumnos(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    
    return render(request , "alumnos.html", {"url":avatares[0].imagen.url})

@login_required
def curso_formulario(request):
    if request.method == "POST":
        mi_formulario = Curso_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso = Curso( nombre=datos["nombre"] , camada=datos["camada"])
            curso.save()
            return render(request , "formulario.html")

    return render(request , "formulario.html")


def buscar_curso(request): 

    return render(request, "buscar_curso.html")


def buscar(request): 

    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        cursos = Curso.objects.filter(nombre__icontains= nombre) #sólo quiero que contengan los que contienen lo que ingrese en el form de búsqueda
        return render(request , "resultado_busqueda.html" , {"cursos": cursos})
    else:
        return HttpResponse("Ingrese el nombre del curso")    

@login_required
def elimina_curso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    cursos = Curso.objects.all()
    return render(request, "cursos.html", {"cursos": cursos}) 

@login_required
def editar(request , id):
    curso = Curso.objects.get(id=id)
    if request.method == "POST":
        mi_formulario = Curso_formulario( request.POST )

        if mi_formulario.is_valid():

            datos = mi_formulario.cleaned_data

            curso.nombre = datos["nombre"]

            curso.camada = datos["camada"]

            curso.save()

            cursos = Curso.objects.all()

            return render(request , "cursos.html" , {"cursos":cursos})
    else:
        mi_formulario = Curso_formulario(initial={"nombre":curso.nombre , "camada":curso.camada}) #initial en un formulario se utiliza para especificar valores iniciales para los campos del formulario,  tiene nombre y camada
    return render( request , "editar_curso.html" , {"mi_formulario": mi_formulario , "curso":curso})

def profesores(request):
    return render(request , "profesores.html")

def ver_profesores(request):
    profesores = Profesores.objects.all()
    print(profesores)  # Verifica si se están recuperando los cursos correctamente
    dicc = {'profesores': profesores}
    plantilla = loader.get_template("profesores.html")
    print(dicc)  # Verifica si los datos se están pasando correctamente a la plantilla
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def profesores_formulario(request):
    if request.method == "POST":
        profesores = Profesores_formulario(request.POST)
        if profesores.is_valid(): #Revisa que los datos vengan como los setee en forms.py
            datos = profesores.cleaned_data #Es un diccionario con los datos limpios y correcto 
            profesores = Profesores(nombre=datos["nombre"], apellido=datos["apellido"], id_comision=datos["id_comision"])
            profesores.save()
            return redirect('ver_profesores.html')  # Redirige a la página deseada después de guardar los datos
    else:
        formulario = Profesores_formulario()
        return render(request, "profesores_formulario.html", {'formulario': formulario})
    
def buscar_profesores(request): 

    return render(request, "buscar_profesores.html")    


def buscarprofesores(request): 

    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        profesores = Profesores.objects.filter(nombre__icontains= nombre) #sólo quiero que contengan los que contienen lo que ingrese en el form de búsqueda
        return render(request , "resultado_busquedaprofesores.html" , {"profesores": profesores})
    else:
        return HttpResponse("Ingrese el nombre del profesor") 
    
def eliminar_profesores(request, id): 
    profesores = Profesores.objects.get(id=id)    
    profesores.delete()

    profesores = Profesores.objects.all()
    return render(request , "profesores.html" , {"profesores":profesores})    

def editar_profesores(request , id):
    profesores = Profesores.objects.get(id=id)
    if request.method == "POST":
        mi_formulario = Profesores_formulario( request.POST )

        if mi_formulario.is_valid():

            datos = mi_formulario.cleaned_data

            profesores.nombre = datos["nombre"]

            profesores.apellido = datos["apellido"]

            profesores.id_comision = datos["id_comision"]

            profesores.save()

            profesores = Profesores.objects.all()

            return render(request , "profesores.html" , {"profesores":profesores})
    else:
        mi_formulario = Profesores_formulario(initial={"nombre":profesores.nombre , "apellido":profesores.apellido , "id_comision":profesores.id_comision}) 
    return render( request , "editar_profesores.html" , {"mi_formulario": mi_formulario , "profesores":profesores})

def ver_alumnos(request):
    alumnos = Alumnos.objects.all()
    print(alumnos)  # Verifica si se están recuperando los cursos correctamente
    dicc = {'alumnos': alumnos}
    plantilla = loader.get_template("alumnos.html")
    print(dicc)  # Verifica si los datos se están pasando correctamente a la plantilla
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

@login_required
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
    if "nombre" in request.GET:
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
    return render(request , "alumnos.html" , {"alumnos":alumnos})    

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
    return render(request , "registro.html" , {"form":form})




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
            # Agregamos un mensaje de éxito a través del sistema de mensajes de Django
            # No redirigimos aquí, permitimos que la plantilla maneje la redirección
        else:
            # Si el formulario no es válido, volvemos a renderizar la página con el formulario y los errores
            messages.error(request, "¡Hubo un error al editar el perfil! Por favor, corrige los errores.")
    else:
        mi_formulario = UserEditForm(initial={"email": usuario.email})
    
    return render(request, "editar_perfil.html", {"miFormulario": mi_formulario, "usuario": usuario, "success_message": success_message})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, "Has cerrado sesión exitosamente.")
        return redirect('home')  # Redirige al usuario a la página de inicio

    # Si la solicitud no es POST, simplemente renderiza la plantilla de logout
    return render(request, 'logout.html')    