# Generated by Django 4.0.1 on 2022-01-18 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('albaranes', '0001_initial'),
        ('facturas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='albaranes',
            name='factura',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='facturas.facturas'),
        ),
    ]
