from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from judicial.models import *
from rest_framework.renderers import JSONRenderer

class AsesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsesorJuridico
        fields = ( 'nombre', 'key' )

class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = ('nombre','url', 'fecha_creacion', 'ultima_modificacion')

class ExpedienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpedienteJuridico
        fields = ('documentos', 'estado', 'numero', 'solicitante', 'key')

class ProvidenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Providencia
        fields = ('gerencia_destino', 'expediente', 'asuento', 'descripcion', 'creacion')

class DictamenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dictamen
        fields = ('expediente', 'fecha_emision', 'asesor', 'descripcion', 'campo_procuraduria')

class OpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpinionJuridica
        fields = ('expediente', 'fecha_emision', 'asesor', 'descripcion')
