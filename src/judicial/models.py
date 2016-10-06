from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ExpedienteJuridico(models.Model):

	documentos = models.ManyToManyField(Documento)
	estado = models.ForeignKey(EstadoExpediente)
	numero = models.IntegerField()
	solicitante = models.ForeignKey(AnalistaJuridico)
	key = models.CharField(unique=True)



class Documento(models.Model):
	nombre = models.CharField()
	url = models.CharField()
	fecha_creacion = models.DateField()
	ultima_modificacion = models.DateField()

class Providencia(models.Model):
	gerencia_destino = models.ForeignKey(Gerencia)
	expediente = models.ForeignKey(ExpedienteJuridico)
	asunto = models.CharField()
	descripcion = models.CharField()
	creacion = models.DateField()

class EstadoExpediente(models.Model):
	gerencia = models.ChoiceField()
	estado = models.CharField()

class Gerencia(models.Model):
	nombre = models.CharField()
	descripcion = models.CharField()

class AnalistaJuridico(AbstractUser):
	nombre = models.CharField()
	key = models.CharField()