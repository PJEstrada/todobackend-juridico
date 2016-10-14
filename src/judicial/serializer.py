from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from judicial.models import AsesorJuridico
from rest_framework.renderers import JSONRenderer

class AsesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsesorJuridico
        fields = ( 'nombre', 'key' )
