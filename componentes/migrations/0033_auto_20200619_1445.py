# Generated by Django 3.0.5 on 2020-06-19 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('componentes', '0032_auto_20200619_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarjeta_evolucion',
            name='muestra',
            field=models.IntegerField(default=15, null=True, verbose_name='Muestra'),
        ),
    ]
