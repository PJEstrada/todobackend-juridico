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
        datos_expediente = {'numero':1,'key':'llavePruebaExpediente','estado': estado.pk,
                                'solicitante': solicitante.pk,
                                'documentos':{'nombre':'test','archivo':file}}
        self.documento_creado = self.client.post('/crear-expediente/',datos_expediente,format='json')

        #----------------------------------------------------------------------
        expediente_dummy = ExpedienteJuridico(numero = 1, key="llavePruebaExp",estado=estado,solicitante=solicitante)
        expediente_dummy.save()
        datos_dictamen = {'expediente': expediente_dummy.pk,
                               'asesor': solicitante.pk,
                               'descripcion': 'Test de descripcion',
                               'campo_procuraduria': 'Procuradoria test'}
        self.dictamen_creado = self.client.post('/crear-dictamen/',datos_dictamen,format='json')

        #----------------------------------------------------------------------
        datos_opinion = {'expediente': expediente_dummy.pk,
                               'asesor': solicitante.pk,
                               'descripcion': 'Test de descripcion'}
        self.opinion_creado = self.client.post('/crear-opinion/',datos_opinion,format='json')

        #---------------------------------------------------------------------
        gerencia = Gerencia(nombre='Gerencia A', descripcion='Esta es una gerencia')
        gerencia.save()

        datos_providencia = {'gerencia_destino': gerencia.pk,
                             'expediente': expediente_dummy.pk,
                             'asunto': 'AsuntoB',
                             'descripcion': 'DescripcionTest'}
        self.providencia_creado = self.client.post('/emitir-providencia/',datos_providencia,format='json')

        #---------------------------------------------------------------------
        estado_dos = EstadoExpediente(gerencia='gerenciaPrueba',estado='Aprobado')
        estado_dos.save()
        datos_actualizar_expediente = {'estado': estado_dos.pk}
        self.expediente_actualizado = self.client.put('/actualizar-expediente/2/',datos_actualizar_expediente)
        #e.documentos.add(documento)

    def test_crear_expediente_201_created_status_code(self):
        self.assertEqual(self.documento_creado.status_code, status.HTTP_201_CREATED)

    def test_crear_expediente_was_created(self):
        self.assertEqual(ExpedienteJuridico.objects.count(), 2)

    def test_obtener_expediente(self):
        self.expediente_obtenido = self.client.get('/expediente/2',format='json',follow=True)
        self.assertEqual(self.expediente_obtenido.status_code, status.HTTP_200_OK)


    def test_crear_dictamen_201_created_status_code(self):
        self.assertEqual(self.dictamen_creado.status_code, status.HTTP_201_CREATED)

    def test_crear_dictamen_was_created(self):
        self.assertEqual(Dictamen.objects.count(), 1)

    # Dado expediente
    def test_obtener_dictamen(self):
        self.dictamen_obtenido = self.client.get('/dictamen/1',format='json',follow=True)
        self.assertEqual(self.dictamen_obtenido.status_code, status.HTTP_200_OK)


    def test_crear_opinion_201_created_status_code(self):
        self.assertEqual(self.opinion_creado.status_code, status.HTTP_201_CREATED)

    def test_crear_opinion_was_created(self):
        self.assertEqual(OpinionJuridica.objects.count(), 1)

    # Dado expediente
    def test_obtener_opinion(self):
        self.opinion_obtenido = self.client.get('/opinion/1',format='json',follow=True)
        self.assertEqual(self.opinion_obtenido.status_code, status.HTTP_200_OK)


    def test_crear_providencia_201_created_status_code(self):
        self.assertEqual(self.providencia_creado.status_code, status.HTTP_201_CREATED)

    def test_crear_providencia_was_created(self):
        self.assertEqual(Providencia.objects.count(), 1)

    def test_actualizar_estado_expediente(self):
        self.assertEqual(self.expediente_actualizado.status_code, status.HTTP_200_OK)
