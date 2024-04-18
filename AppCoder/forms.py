from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Curso_formulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    camada = forms.IntegerField()


class Profesores_formulario(forms.Form): 

    nombre = forms.CharField(max_length=40) 
    apellido = forms.CharField(max_length=40) 
    id_comision = forms.IntegerField()     

class Alumnos_formulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    camada = forms.IntegerField()

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput())  
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput())  


    class Meta: #asociamos metadatos al form
        model = User
        fields = ['email', 'password1', 'password2']
        help_texts = {k: "" for k in fields } #k es una key 
    
