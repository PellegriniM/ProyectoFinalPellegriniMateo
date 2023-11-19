from django import forms
from ckeditor.fields import RichTextFormField

class BaseNoticiaFormulario(forms.Form):
    autor = forms.CharField(max_length=30)
    asunto = forms.CharField(max_length=30)
    descripcion = RichTextFormField()
    fecha_creacion = forms.DateField()
    

class CrearNoticiaFormulario(BaseNoticiaFormulario):
    ...


class ActualizarNoticiaFormulario(BaseNoticiaFormulario):
    ...



class BusquedaNoticiaFormulario(forms.Form):
    asunto = forms.CharField(max_length=30, required=False)