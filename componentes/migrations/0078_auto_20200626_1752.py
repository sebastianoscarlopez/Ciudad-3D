# Generated by Django 3.0.5 on 2020-06-26 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('componentes', '0077_remove_indicador_id_indicador_anterior'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dona',
            name='id_indicador_bk',
            field=models.CharField(blank=True, default='', max_length=256, null=True, verbose_name='Id Indicador Bk'),
        ),
        migrations.AlterField(
            model_name='grafico_cartesiano',
            name='id_indicador_bk',
            field=models.CharField(blank=True, default='', max_length=256, null=True, verbose_name='Id Indicador Bk'),
        ),
        migrations.AlterField(
            model_name='tarjeta',
            name='id_indicador_bk',
            field=models.CharField(blank=True, default='', max_length=256, null=True, verbose_name='Id Indicador Bk'),
        ),
    ]
