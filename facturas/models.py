from django.db import models
#from internationalflavor.iban import IBANField

from contactos.models import Empresa


IRPF =[
    (0, 'No aplica'),
    (-0.07, '7%'),
    (-0.15, '15%'),
]
TIPOS_FACTURA=[
    ('ORD', 'Factura ordinaria'),
    ('RET', 'Factura rectificativa'),
    ('REC', 'Factura recapitulativa'),
    ('PRO', 'Factura proforma'),
]

FORMAS_PAGO =[
    ('transferencia a la vista', 'Transferencia a la vista'),
    ('transferencia 15 días', 'Transferencia 15 días'),
    ('transferencia 30 días', 'Transferencia 30 días'),
    ]
CUENTAS_PAGO =[
    ('cuenta de prueba', 'Cuenta'),
    ('efectivo', 'Efectivo'),
    ]

class FacturasManager(models.Manager):
    def filter_by_year(self, year):
        return self.filter(self.fecha_albaran.year()==year)

    def filter_by_year_type(self, year, tipo_fact):
        return self.filter(self.fecha_albaran.year()==year, self.tipo==tipo_fact)


class Facturas(models.Model):
    fecha_factura = models.DateField(auto_now_add=True, verbose_name='Fecha albarán')
    no_factura = models.CharField(
        max_length=20,
        verbose_name='Número de factura',
        unique_for_year='fecha',
        null=False, blank= False)
    tipo=models.CharField(
        max_length=3,
        verbose_name='Serie',
        default='FOR',
        choices=TIPOS_FACTURA,)
    cliente = models.ForeignKey(
        Empresa,
        verbose_name='Cliente',
        on_delete=models.PROTECT)
    base_imp = models.DecimalField(
        'Base Imponible',
        max_digits=9,
        decimal_places=2)
    cuota_iva = models.DecimalField(
        'Cuota IVA',
        max_digits=9,
        decimal_places=2)
    tipo_irpf= models.DecimalField(
        'Tipo IRPF', max_digits=9, decimal_places=2)
    cuota_irpf=  models.DecimalField(
        'Cuota IRPF',
        max_digits=3,
        decimal_places=2,
        choices=IRPF)
    importe = models.DecimalField(
        'Importe Total',
        max_digits=9,
        decimal_places=2)
    pagado= models.BooleanField(
        verbose_name='Factura Pagada',
        default=False,)
    forma_pago=models.CharField(
        max_length=40,
        verbose_name='Forma de pago',
        choices=FORMAS_PAGO)
    cuenta_abono=models.CharField(
        max_length=25,
        verbose_name='Cuenta de abono',
        choices=CUENTAS_PAGO)



    def save(self, *args, **kwargs):
        if not self.no_factura:
            n_facturas_ano = Facturas.objects.filter_by_year(self.fecha_entrada).count()
            nuevo_albaran = (str (n_facturas_ano+1).zfill(4)+'/'+ self.fecha_entrada.strftime("%y"))
            self.no_albaran = nuevo_albaran
        
            super().save(*args, **kwargs)

    class Meta():
        verbose_name = 'Albarán'
        verbose_name_plural = 'Albaranes'

    def __str__(self):
        """Unicode representation of Albaranes."""
        return self.no_albaran
