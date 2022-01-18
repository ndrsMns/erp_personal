import decimal
from django.test import TestCase
from django.utils import timezone

from contactos.models import Empresa
from .models import Albaranes, ItemsAlbaranes


class BaseModelTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super(BaseModelTestCase, cls).setUpClass()

        cls.empresa = Empresa.objects.create(
            denominacion='Empresa',
            calle='Corcubion',
            nif='B70583539',)
        cls.albaran = Albaranes.objects.create(
            fecha_albaran=timezone.now(),
            cliente=cls.empresa, 
            factura= None,)
        cls.item1=ItemsAlbaranes.objects.create(
            albaran=cls.albaran,
            concepto='concepto1',
            cantidad=2.0,
            p_unit=2.0,
            tipo_iva=10.0,)
        cls.item2=ItemsAlbaranes.objects.create(
            albaran=cls.albaran,
            concepto='concepto2',
            cantidad=10.0,
            p_unit=10.0,
            tipo_iva=21.0,)
        cls.albaran2 = Albaranes.objects.create(
            fecha_albaran=timezone.now(),
            cliente=cls.empresa, 
            factura= None,)
        cls.item3=ItemsAlbaranes.objects.create(
            albaran=cls.albaran2,
            concepto='concepto3',
            cantidad=2.0,
            p_unit=10.0,
            tipo_iva=10.0,)
        cls.item4=ItemsAlbaranes.objects.create(
            albaran=cls.albaran2,
            concepto='concepto4',
            cantidad=10.0,
            p_unit=10.0,
            tipo_iva=10.0,)

class AlbaranModelTestCase(BaseModelTestCase):
    def test_items_created(self):
        self.assertEqual(ItemsAlbaranes.objects.get(id=1).concepto, self.item1.concepto)
        self.assertEqual(ItemsAlbaranes.objects.get(id=2).concepto, self.item2.concepto)
        self.assertEqual(ItemsAlbaranes.objects.get(id=1).albaran.cliente, self.item1.albaran.cliente)


    def test_albaran_created(self):
        self.assertEqual(Albaranes.objects.get(id=1).fecha_albaran, self.albaran.fecha_albaran.date())
        self.assertEqual(Albaranes.objects.get(id=1).cliente.denominacion, self.albaran.cliente.denominacion)

    def test_no_alb(self):
        self.assertEqual(Albaranes.objects.get(id=1).no_albaran, '0001/'+timezone.now().strftime('%y'))
        self.assertEqual(Albaranes.objects.get(id=2).no_albaran, '0002/'+timezone.now().strftime('%y'))

    def test_properties_items(self):
        self.assertNotEqual(ItemsAlbaranes.objects.get(id=1).base_imponible, decimal.Decimal(4.40))
        self.assertAlmostEqual(ItemsAlbaranes.objects.get(id=1).base_imponible, decimal.Decimal(4.00), 2)
        self.assertAlmostEqual(ItemsAlbaranes.objects.get(id=1).cuota_iva, decimal.Decimal(0.40),2)
        self.assertAlmostEqual(ItemsAlbaranes.objects.get(id=1).importe, decimal.Decimal(4.40), 2)
    
    def test_properties_albaranes(self):
        print(Albaranes.objects.get(id=1).base_imp_alb)
        print(Albaranes.objects.get(id=2).base_imp_alb)
        self.assertAlmostEqual(Albaranes.objects.get(id=1).base_imp_alb, decimal.Decimal(104.00), 2)
        print(Albaranes.objects.get(id=1).cuota_iva_alb)
        print(Albaranes.objects.get(id=2).cuota_iva_alb)
        self.assertAlmostEqual(Albaranes.objects.get(id=1).cuota_iva_alb, decimal.Decimal(21.4),2)
        self.assertAlmostEqual(Albaranes.objects.get(id=1).importe_alb, decimal.Decimal(125.40), 2)