from django.db import models
from internationalflavor.vat_number import VATNumberField





class Empresa(models.Model):
    '''Tabla de empresas'''
    denominacion = models.CharField(
        verbose_name='Denominación social/Apellidos y nombre',
        max_length=60)
    n_comercial = models.CharField(
        verbose_name='Nombre comercial',
        max_length=50,
        blank=True,
        null=True,)
    calle = models.CharField(
        verbose_name='Calle',
        max_length=100)
    calle2 = models.CharField(
        verbose_name='Calle 2',
        max_length=100,
        blank=True, null=True)
    ciudad = models.CharField(
        verbose_name='Ciudad',
        max_length=30,
        blank=True, null=True)
    provincia = models.CharField(
        verbose_name='Provincia',
        max_length=20,
        blank=True, null=True)
    cp = models.CharField(
        verbose_name='Código Postal',
        max_length=8,
        blank=True, null=True)
    pais = models.CharField(
        verbose_name='País',
        max_length=20,
        default='España')
    nif = VATNumberField(countries=['ES', 'PT'],
        verbose_name='NIF',
        max_length=15,
        unique=True,
        error_messages={'unique': 'Ya existe otro contacto con ese NIF'})
    email = models.EmailField(
        verbose_name='Email',
        blank=True, null=True)
    tfno = models.CharField(
        verbose_name='Teléfono ejemplo +34000000000',
        max_length=12,
        blank=True, null=True)
    movil = models.CharField(
        verbose_name='Móvil ejemplo +34000000000',
        max_length=12,
        blank=True, null=True)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        if self.n_comercial:
            return f'{self.n_comercial}'
        else:
            return f'{self.denominacion}'


class Contacto(models.Model):
    nombre = models.CharField(
        max_length=50,
        verbose_name='Nombre de contacto',
        blank=False, null=False, )
    empresa = models.ForeignKey(
        Empresa,
        on_delete=models.CASCADE,
        related_name='empresas',)
    email = models.EmailField(
        verbose_name='Email',
        blank=True, null=True)
    tfno = models.CharField(
        verbose_name='Teléfono ejemplo +34000000000',
        max_length=12,
        blank=True, null=True)

    def __str__(self):
        return str(self.nombre) + " " + str(self.empresa)
