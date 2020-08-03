# Generated by Django 3.0.6 on 2020-06-25 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0032_sube_transporte_publico_evolucion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sube_colectivo_variacion_dia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(blank=True, null=True, verbose_name='Fecha')),
                ('dato', models.CharField(max_length=256, null=True, verbose_name='Cantidad')),
            ],
            options={
                'db_table': 'dataset_sube_colectivo_variacion_dia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sube_ffcc_variacion_dia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(blank=True, null=True, verbose_name='Fecha')),
                ('dato', models.CharField(max_length=256, null=True, verbose_name='Cantidad')),
            ],
            options={
                'db_table': 'dataset_sube_ffcc_variacion_dia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sube_subte_variacion_dia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(blank=True, null=True, verbose_name='Fecha')),
                ('dato', models.CharField(max_length=256, null=True, verbose_name='Cantidad')),
            ],
            options={
                'db_table': 'dataset_sube_subte_variacion_dia',
                'managed': False,
            },
        ),
    ]
