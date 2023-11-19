from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class MiFormularioDeCreacion(UserCreationForm):
    first_name = forms.CharField(max_length=20, label='Nombre', widget=forms.TextInput)
    last_name = forms.CharField(max_length=20, label='Apellido', widget=forms.TextInput)
    email = forms.EmailField()
    password1 = forms.CharField(label='Contrasenia', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contrasenia', widget=forms.PasswordInput)
    
    
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2']
        help_texts = {key: '' for key in fields}


class MiFormularioDeEdicion(UserChangeForm):
    password = None
    email = forms.EmailField(label='Cambiar email', required=False)
    first_name = forms.CharField(label='Cambiar nombre', required=False)
    last_name = forms.CharField(label='Cambiar apellido', required=False)
    biografia = forms.CharField(max_length=300, required=False, widget=forms.Textarea)
    avatar = forms.ImageField(required=False)
    
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'biografia','avatar']
        help_texts = {key: '' for key in fields}