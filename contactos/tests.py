from django.test import TestCase

from .models import Empresa, Contacto


class BaseModelTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super(BaseModelTestCase, cls).setUpClass()

        cls.empresa = Empresa.objects.create(
            denominacion='Empresa',
            calle='Corcubion',
            nif='B70583539',
            pais='España',
            ciudad='Corcubion')
        cls.contacto = Contacto.objects.create(
            empresa=cls.empresa,
            nombre='Pepe',
            email='pepe@pepito.com',
            tfno='+34000000000')


class EmpresaModelTestCase(BaseModelTestCase):
    def test_empresa_created(self):
        self.assertEqual(Empresa.objects.get(id=1).denominacion, self.empresa.denominacion)
        self.assertEqual(Empresa.objects.get(id=1).calle, self.empresa.calle)
        self.assertEqual(Empresa.objects.get(id=1).nif, self.empresa.nif)

    def test_empresa_str(self):
        self.assertEqual(Empresa.objects.get(id=1), self.empresa)


class ContactoModelTestCase(BaseModelTestCase):
    def test_contacto_created(self):
        self.assertEqual(Contacto.objects.get(id=1).nombre, self.contacto.nombre)
        self.assertEqual(Contacto.objects.get(id=1).email, self.contacto.email)
        self.assertEqual(Contacto.objects.get(id=1).tfno, self.contacto.tfno)
        self.assertEqual(Contacto.objects.get(id=1).empresa.calle, self.contacto.empresa.calle)
        self.assertEqual(Contacto.objects.get(id=1).empresa.denominacion, self.contacto.empresa.denominacion)

    def test_contacto_str(self):
        print(str(Contacto.objects.get(id=1)), str(
            self.contacto.nombre) + " " + str(self.empresa))
        self.assertEqual(str(Contacto.objects.get(id=1)), str(
            self.contacto.nombre) + " " + str(self.empresa))
