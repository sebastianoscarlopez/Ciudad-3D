# Generated by Django 3.0.5 on 2020-07-02 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db_views', '0004_auto_20200701_1905'),
        ('componentes', '0087_auto_20200629_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='dona',
            name='view_asociada',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='db_views.Vista'),
        ),
        migrations.AddField(
            model_name='grafico_cartesiano',
            name='view_asociada',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='db_views.Vista'),
        ),
        migrations.AddField(
            model_name='tarjeta',
            name='view_asociada',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='db_views.Vista'),
        ),
    ]
