from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.2asdg

#class AsesorJuridico(AbstractUser):
class AsesorJuridico(models.Model):
	nombre = models.CharField(max_length=50)
	key = models.CharField(max_length=50)

class Documento(models.Model):
	nombre = models.CharField(max_length=50)
	archivo = models.FileField(blank=True)
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	ultima_modificacion = models.DateTimeField(auto_now_add=True)

class EstadoExpediente(models.Model):
	gerencia = models.CharField(max_length=50)
	estado = models.CharField(max_length=50)

class Gerencia(models.Model):
	nombre = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=50)

class ExpedienteJuridico(models.Model):
	# Alguna otra informacion relevante al contexto juridico ?
	documentos = models.ManyToManyField(Documento)
	estado = models.ForeignKey(EstadoExpediente)
	numero = models.IntegerField()
	solicitante = models.ForeignKey(AsesorJuridico)
	key = models.CharField(unique=True, max_length=100)
	numero_instancia = models.IntegerField(null=True, blank=True)

class Providencia(models.Model):
	# La providencia contiene alguna otra informacion?
	gerencia_destino = models.ForeignKey(Gerencia)
	expediente = models.ForeignKey(ExpedienteJuridico)
	asunto = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=50)

	creacion = models.DateTimeField(auto_now_add=True)
	#TODO el maldito usuarioooooooooooooooooooooooooooooooooooooooooooo
	archivo = models.FileField(blank=True)
	numero_instancia = models.IntegerField(null=True, blank=True)

class Dictamen(models.Model):
	expediente = models.ForeignKey(ExpedienteJuridico)
	fecha_emision = models.DateTimeField(auto_now_add=True)
	asesor = models.ForeignKey(AsesorJuridico)
	descripcion = models.CharField(max_length=50)
	campo_procuraduria = models.CharField(max_length=50)
	numero_instancia = models.IntegerField(null=True, blank=True)

class OpinionJuridica(models.Model):
	expediente = models.ForeignKey(ExpedienteJuridico)
	fecha_emision = models.DateTimeField(auto_now_add=True)
	asesor = models.ForeignKey(AsesorJuridico)
	descripcion = models.CharField(max_length=50)
	numero_instancia = models.IntegerField(null=True, blank=True)


# mi comment
