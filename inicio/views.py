from django.shortcuts import render, redirect

from inicio.models import Noticia
from inicio.forms import CrearNoticiaFormulario,BusquedaNoticiaFormulario,ActualizarNoticiaFormulario

from django.contrib.auth.decorators import login_required


def inicio(request):
    return render(request, 'inicio/inicio.html', {})

def AboutMe(request):
    return render(request, 'inicio/AboutMe.html', {})


def noticia(request):
    formulario = BusquedaNoticiaFormulario(request.GET)
    if formulario.is_valid():
        asunto_a_buscar = formulario.cleaned_data.get('asunto')
        listado_de_noticias = Noticia.objects.filter(asunto__icontains = asunto_a_buscar)

    return render(request, 'inicio/noticia.html', {'listado_de_noticias': listado_de_noticias})

@login_required
def crear_noticia(request):
    if request.method == "POST":
        formulario = CrearNoticiaFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            autor = info_limpia.get('autor')
            asunto = info_limpia.get('asunto')
            descripcion = info_limpia.get('descripcion')
            fecha_creacion = info_limpia.get('fecha_creacion')
            
            
            noticia = Noticia(autor=autor, asunto=asunto, descripcion=descripcion, fecha_creacion=fecha_creacion)
            noticia.save()

            return redirect('noticias')

    formulario = CrearNoticiaFormulario()

    return render(request, 'inicio/crear_noticia.html',{'formulario': formulario})

@login_required
def eliminar_noticia(request, noticia_id):
    noticia_a_eliminar = Noticia.objects.get(id=noticia_id)
    noticia_a_eliminar.delete()
    return redirect("noticias")


@login_required
def actualizar_noticia(request, noticia_id):
    noticia_a_actualizar = Noticia.objects.get(id=noticia_id)
    
    if request.method == "POST":
        formulario = ActualizarNoticiaFormulario(request.POST)
        if formulario.is_valid():
            info_nueva = formulario.cleaned_data
            
            noticia_a_actualizar.autor = info_nueva.get('autor')
            noticia_a_actualizar.asunto = info_nueva.get('asunto')
            noticia_a_actualizar.descripcion = info_nueva.get('descripcion')
            noticia_a_actualizar.fecha_creacion = info_nueva.get('fecha_creacion')
            noticia_a_actualizar.iamgen = info_nueva.get('imagen')
            
            
            noticia_a_actualizar.save()
            return redirect('noticias')
        else:
            return render(request, 'ínicio/actualizar_noticia.html', {'formulario': formulario})
    
    formulario = ActualizarNoticiaFormulario(initial={'autor': noticia_a_actualizar.autor,'asunto': noticia_a_actualizar.asunto, 'descripcion': noticia_a_actualizar.descripcion, 'fecha_creacion': noticia_a_actualizar.fecha_creacion, 'imagen': noticia_a_actualizar.imagen})
    return render(request, 'inicio/actualizar_noticia.html', {'formulario': formulario})


def detalle_noticia(request, noticia_id):
    noticia = Noticia.objects.get(id=noticia_id)
    return render (request, 'inicio/detalle_noticia.html', {'noticia': noticia})