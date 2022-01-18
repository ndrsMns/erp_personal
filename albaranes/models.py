from decimal import Decimal
from django.db import models
from django.utils import timezone
from django.db.models import Sum, F

from abstract.models import ProductAbstractModel
from contactos.models import Empresa
from facturas.models import Facturas


class AlbaranesManager(models.Manager):
    def filter_by_year(self, year):
        return self.filter(fecha_albaran__year__exact=year)


class Albaranes(models.Model):
    fecha_albaran = models.DateField(
        default=timezone.now(),
        verbose_name='Fecha albarán')
    no_albaran = models.CharField(
        max_length=10,
        verbose_name='Número de albarán',
        unique_for_year='fecha',
        null=False, blank= False)
    cliente = models.ForeignKey(Empresa,
        verbose_name='Cliente', 
        on_delete=models.PROTECT,)
    factura= models.ForeignKey(Facturas,
        on_delete=models.DO_NOTHING,
        null=True, blank=True,)

    objects = AlbaranesManager()

    @property
    def base_imp_alb(self):
        base_items = ItemsAlbaranes.objects.annotate(
            base_imponible=F('cantidad') * F('p_unit')).filter(albaran=self.id)
        return base_items.aggregate(Sum('base_imponible'))['base_imponible__sum']


    @property
    def cuota_iva_alb(self):
        base_items = ItemsAlbaranes.objects.annotate(
            cuota_iva=F('cantidad') * F('p_unit')*F('tipo_iva')*Decimal(0.01)).filter(albaran=self.id)
        return base_items.aggregate(Sum('cuota_iva'))['cuota_iva__sum']

    @property
    def importe_alb(self):
        return self.base_imp_alb + self.cuota_iva_alb

    def save(self, *args, **kwargs):
        if not self.no_albaran:
            n_albarans_ano = Albaranes.objects.filter_by_year(self.fecha_albaran.year).count()
            nuevo_albaran = (str (n_albarans_ano+1).zfill(4)+'/'+ self.fecha_albaran.strftime("%y"))
            self.no_albaran = nuevo_albaran
            super().save(*args, **kwargs)


    class Meta():
        verbose_name = 'Albarán'
        verbose_name_plural = 'Albaranes'

    def __str__(self):
        """Unicode representation of Albaranes."""
        return str(self.no_albaran)


class ItemsAlbaranes(ProductAbstractModel):
    """Model definition for ItemsAlbaranes."""

    albaran = models.ForeignKey(Albaranes, 
    on_delete=models.CASCADE,
    related_name= 'items',
    verbose_name='Albarán')

    class Meta:
        """Meta definition for ItemsAlbaranes."""
        verbose_name = 'Item Albaranes'
        verbose_name_plural = 'Items Albaranes'
