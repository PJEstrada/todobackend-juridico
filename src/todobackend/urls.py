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
from judicial.models import AsesorJuridico
from judicial import views
class AsesorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AsesorJuridico
        fields = ( 'nombre', 'key' )

class AsesorViewSet(viewsets.ModelViewSet):
    queryset = AsesorJuridico.objects.all()
    serializer_class = AsesorSerializer

#Rutas definidass
router = routers.DefaultRouter()
router.register(r'users', AsesorViewSet)
#router.register(r'users/(?P<id>[0-9]+)/$', views.user_detail)
#router.register(r'^users-view/$', views.snippet_list)
#asesor_view = AsesorViewSet.as_view({'get':'retrieve'})

urlpatterns = [
    url(r'^users-view/$', views.snippet_list),
    url(r'^', include(router.urls)), #prueba de routers, contiene todas las rutas predefinidas
    url(r'^', include('todo.urls')),
    #url(r'^api-auth/', AsesorViewSet),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include('rest_framework_docs.urls')),

]
