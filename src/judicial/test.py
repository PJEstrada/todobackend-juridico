from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from judicial.serializer import *
from judicial.models import *


class TestExpediente(APITestCase):
    """
    Test para probar todo lo relacionado a expediente
    """
    def setUp(self):
        file = open('myfile.txt', 'w+')
        solicitante = AsesorJuridico(nombre='Miguel-Novella',key='123')
        solicitante.save()
        estado = EstadoExpediente(gerencia='gerenciaPrueba',estado='Pendiente')
        estado.save()
        solicitante_serializer = AsesorSerializer(solicitante)
        self.datos_expediente = {'numero':1,'key':'llavePruebaExpediente','estado': estado.pk,
                                'solicitante': solicitante.pk,
                                'documentos':{'nombre':'test','archivo':file}}
        self.documento_creado = self.client.post('/crear-expediente/',self.datos_expediente,format='json')
        #e.documentos.add(documento)

    def test_crear_expediente_201_created_status_code(self):
        self.assertEqual(self.documento_creado.status_code, status.HTTP_201_CREATED)

    def test_crear_expediente_was_created(self):
        self.assertEqual(ExpedienteJuridico.objects.count(), 1)

    def test_obtener_dictamen_dado_expediente(self):
        pass

    def test_obtener_opinion_dado_dictamen(self):
        pass

    def test_obtener_expediente(self):
        pass

    def test_actualizar_estado_expediente(self):
        pass

class TestOpiniones(APITestCase):
    """
    para opiniones
    """

    def setUp(self):
        pass

    def test_crear_opinion(self):
        pass

class TestDictamen(APITestCase):
    """
    para dictamenes
    """
    def setUp(self):
        pass

    def test_crear_dictamen(self):
        pass
