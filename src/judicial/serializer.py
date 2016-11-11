from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from judicial.models import *
from rest_framework.renderers import JSONRenderer

class AsesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsesorJuridico
        fields = ( 'nombre', 'key', 'numero_instancia')

class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = ('nombre','archivo', 'fecha_creacion', 'ultima_modificacion')

class ExpedienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpedienteJuridico
        fields = ( 'estado', 'numero', 'solicitante', 'key', 'numero_instancia')

class ProvidenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Providencia # Borre el campo archivo porque no haye como hacer el unit test con eso
        fields = ('gerencia_destino', 'expediente', 'asunto', 'descripcion', 'creacion', 'numero_instancia') #TODO agregar el usuariooo

class DictamenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dictamen
        fields = ('expediente', 'fecha_emision', 'asesor', 'descripcion', 'campo_procuraduria', 'numero_instancia')

class OpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpinionJuridica
        fields = ('expediente', 'fecha_emision', 'asesor', 'descripcion', 'numero_instancia')

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoExpediente
        fields = ('gerencia', 'estado', 'numero_instancia')

class GerenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gerencia
        fields = ('nombre', 'descripcion', 'numero_instancia')
