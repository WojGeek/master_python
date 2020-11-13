"""Aprendiendo_Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# importar app con mis vistas
#from miapp import views
# otra manera de vincular 
import miapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', miapp.views.index, name='index'),
    path('inicio/', miapp.views.index, name='index'),
    path('pagina/', miapp.views.pagina, name='pagina'),
    path('hola-mundo/', miapp.views.hola_mundo, name="hola_mundo"),
    path('contacto/', miapp.views.contacto, name="contacto"),
    path('contacto/<str:nombre>', miapp.views.contacto, name="contacto"),
    path('contacto/<str:nombre>/<str:apellido>', miapp.views.contacto, name="contacto"),
    path('visitar_otra_pagina/', miapp.views.visitar_otra_pagina, name="visitar_otra_pagina"),
    path('visitar_otra_pagina/<int:redirigir>', miapp.views.visitar_otra_pagina, name="visitar_otra_pagina"),
    path('visitar_google/', 
    miapp.views.visitar_google, name="visitar_google"),
    path('creararticulo/', miapp.views.crear_articulo, name='creararticulo'),
    path('creararticulo/<str:title>/<str:content>/<str:public>', miapp.views.crear_articulo, name='creararticulo'),
    path('articulo', miapp.views.articulo, name='articulo'),
    path('articulo/<str:id>', miapp.views.articulo, name='articulo'),
    path('actualiza/<int:id>', miapp.views.actualizar_articulo),
    path('articulos', miapp.views.articulos, name='articulos'),
    path('borrararticulo/<int:id>', miapp.views.borrar_articulo, name='borrar'),
    path('createarticle', miapp.views.create_article, name='create'),
    path('savearticle', miapp.views.save_article, name='save'),
    path('create-full-article', miapp.views.create_full_article, name='create_full'),
]

"""
# Es importante!  Agregar en el path la parte 'name' para indicar la ruta y de ese modo
   no perder la asociacion aunque se cambiase las opciones del   menu

        path(....., menu="nombre")

"""