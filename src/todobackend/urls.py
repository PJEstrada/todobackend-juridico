"""todobackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from judicial import views as views

#Rutas definidass
#router = routers.SimpleRouter()
#router.register(r'asesores-api', views.AsesorViewSet)
#router.register(r'dictamen', views.dictamen_dado_expediente, base_name="dict")
#router.register(r'asesores', views.asesores, base_name="ases")
#asesor_view = AsesorViewSet.as_view({'get':'retrieve'})

urlpatterns = [
    url(r'^users-view/$', views.asesores),
    url(r'^estados/$', views.estados),
    url(r'^dictamen/(?P<id>[0-9]+)/$', views.dictamen_dado_expediente),
    url(r'^opinion/(?P<id>[0-9]+)/$', views.opinion_dado_expediente),
    url(r'^providencia/(?P<id>[0-9]+)/$', views.providencia_dado_expediente),
    url(r'^expediente/(?P<id>[0-9]+)/$', views.obtener_expediente),
    url(r'^expedientes-asesor/(?P<id>[0-9]+)/$', views.expedientes_dado_asesor),
    url(r'^crear-opinion/', views.crear_opinion),
    url(r'^crear-dictamen/', views.crear_dictamen),
    url(r'^emitir-providencia/', views.emitir_providencia),
    url(r'^crear-expediente/', views.crear_expediente), #Eliminar
    url(r'^crear-estado/', views.crear_estado), #Eliminar
    url(r'^crear-usuario/', views.crear_usuario), #Eliminar
    url(r'^actualizar-expediente/(?P<id>[0-9]+)/$', views.update_estado_expediente),
    #   url(r'^', include('todo.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include('rest_framework_docs.urls')),

]
