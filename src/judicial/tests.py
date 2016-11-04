from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from judicial.serializer import *
from judicial.models import *


class TestJuridicoModulo(APITestCase):
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

    def test_obtener_expediente(self):
        self.expediente_obtenido = self.client.get('/expediente/1',format='json',follow=True)
        self.assertEqual(self.expediente_obtenido.status_code, status.HTTP_200_OK)

    def test_crear_dictamen(self):
        #self.datos_dictamen = {'expediente':self.expediente_obtenido,
        #                       'asesor': solicitante.pk,
        #                       'descripcion': 'Test de descripcion',
        #                       'campo_procuraduria': 'Procuradoria test'}
        #self.dictamen_creado = self.client.post('/crear-dictamen/',self.datos_dictamen,format='json')
        #self.assertEqual(self.dictamen_creado.status_code, status.HTTP_201_CREATED)
        pass

    def test_crear_opinion(self):
        pass

    def test_obtener_dictamen_dado_expediente(self):
        pass

    def test_obtener_opinion_dado_dictamen(self):
        pass

    def test_actualizar_estado_expediente(self):
        pass
