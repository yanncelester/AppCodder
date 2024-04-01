from django.shortcuts import render, redirect
from AppCoder.models import Curso
from django.http import HttpResponse
from django.template import loader
from AppCoder.forms import Curso_formulario
from django.http import Http404
from AppCoder.forms import Profesores_formulario  
from AppCoder.models import Profesores 
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from AppCoder.models import Alumnos
from AppCoder.forms import Alumnos_formulario 




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
    curso = Curso.objects.all()
    print(curso)  # Verifica si se están recuperando los cursos correctamente
    dicc = {'curso': curso}
    plantilla = loader.get_template("cursos.html")
    print(dicc)  # Verifica si los datos se están pasando correctamente a la plantilla
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def ver_curso(request):
    try:
        curso = Curso.objects.all()
        dicc = {'curso': curso}
        plantilla = loader.get_template("cursos.html")
        documento = plantilla.render(dicc)
        return HttpResponse(documento)
    except Curso.DoesNotExist:
        raise Http404("No existen cursos en la base de datos")  # Mensaje de error personalizado
    except Exception as e:
        print(f"Error en la vista ver_curso: {e}")  # Imprimir el error en la consola para depurar
        raise Http404("Error en la vista ver_curso")  # Mensaje de error general

def alumnos(request):
    return render(request , "alumnos.html")

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
    
def elimina_curso(request , id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    curso = Curso.objects.all()
    return render(request , "cursos.html" , {"curso":curso})    


def editar(request , id):
    curso = Curso.objects.get(id=id)
    if request.method == "POST":
        mi_formulario = Curso_formulario( request.POST )

        if mi_formulario.is_valid():

            datos = mi_formulario.cleaned_data

            curso.nombre = datos["nombre"]

            curso.camada = datos["camada"]

            curso.save()

            curso = Curso.objects.all()

            return render(request , "cursos.html" , {"curso":curso})
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
    
def eliminar_alumnos(request, id): 
    alumnos = Alumnos.objects.get(id=id)    
    alumnos.delete()

    alumnos = Alumnos.objects.all()
    return render(request , "alumnos.html" , {"alumnos":alumnos})    

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