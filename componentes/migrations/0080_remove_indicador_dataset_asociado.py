# Generated by Django 3.0.5 on 2020-06-29 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('componentes', '0079_auto_20200626_1755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='indicador',
            name='dataset_asociado',
        ),
    ]
