from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from judicial.serializer import *


class TestExpediente(APITestCase):
    """
    Test para probar todo lo relacionado a expediente
    """
    def setUp(self):
        self.data = {'username': 'mike', 'first_name': 'Mike', 'last_name': 'Tyson'}

    def test_crear_expediente(self):
        pass

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
