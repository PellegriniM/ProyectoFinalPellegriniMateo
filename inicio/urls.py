from django.urls import path
from inicio.views import inicio, AboutMe, noticia, crear_noticia, detalle_noticia, eliminar_noticia,actualizar_noticia

urlpatterns = [
    path('', inicio, name='inicio'),
    path('SobreMi', AboutMe, name='AboutMe'),
    path('noticias/', noticia, name='noticias'),
    path('noticias/crear/', crear_noticia, name='crear_noticia'), #Creacion de noticias
    path('noticias/<int:noticia_id>/', detalle_noticia, name='detalle_noticia'), #Detalle noticias
    path('noticias/<int:noticia_id>/eliminar/', eliminar_noticia, name='eliminar_noticia'), #Eliminar noticias
    path('noticias/<int:noticia_id>/actualizar/', actualizar_noticia, name='actualizar_noticia'), #Actualizar noticias
]
