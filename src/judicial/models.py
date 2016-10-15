from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.2asd

class AsesorJuridico(AbstractUser):
	nombre = models.CharField(max_length=50)
	key = models.CharField(max_length=50)

class Documento(models.Model):
	nombre = models.CharField(max_length=50)
	url = models.CharField(max_length=100)
	fecha_creacion = models.DateField()
	ultima_modificacion = models.DateField()

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

class Providencia(models.Model):
	# La providencia contiene alguna otra informacion?
	gerencia_destino = models.ForeignKey(Gerencia)
	expediente = models.ForeignKey(ExpedienteJuridico)
	asunto = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=50)
	creacion = models.DateField()

class Dictamen(models.Model):
	expediente = models.ForeignKey(ExpedienteJuridico)
	fecha_emision = models.DateField()
	asesor = models.ForeignKey(AsesorJuridico)
	descripcion = models.CharField(max_length=50)
	campo_procuraduria = models.CharField(max_length=50)

class OpinionJuridica(models.Model):
	expediente = models.ForeignKey(ExpedienteJuridico)
	fecha_emision = models.DateField()
	asesor = models.ForeignKey(AsesorJuridico)
	descripcion = models.CharField(max_length=50)


# mi comment
