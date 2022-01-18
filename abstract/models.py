from django.db import models

UNIDADES =[
    ('kg', 'kilos'),
    ('ud', 'Unidades'),
    ('l', 'litros'),
    ('m3', 'metros cúbicos'),
    ('ml', 'metros lineales'),
    ('', 'Sin unidades'),
]

IVA =[
    (0, '0%'),
    (4, '4%'),
    (10, '10%'),
    (21, '21%'),
]


class ProductAbstractModel(models.Model):
    """Model definition for ProductAbtractModel."""

    concepto = models.TextField('Concepto', max_length=200)
    unidad = models.CharField('Unidad', max_length=3, choices=UNIDADES)
    cantidad = models.DecimalField('Cantidad', max_digits=9, decimal_places=3)
    p_unit = models.DecimalField('Precio unitario', max_digits=9, decimal_places=2)
    tipo_iva= models.DecimalField('IVA', max_digits=4, decimal_places=2, choices=IVA, null=True)


    @property
    def base_imponible(self):
        return round(self.cantidad * self.p_unit, 2)
    
    @property
    def cuota_iva(self):
        return round(self.base_imponible * self.tipo_iva /100,2)
    
    @property
    def importe(self):
        return round(self.base_imponible + self.cuota_iva, 2)

    class Meta:
        """Meta definition for ProductAbstractModel."""
        abstract = True

    def __str__(self):
        """Unicode representation of ProductAbstractModel."""
        return self.concepto


