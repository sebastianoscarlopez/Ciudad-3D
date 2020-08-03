# Generated by Django 3.0.6 on 2020-06-25 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('componentes', '0070_auto_20200625_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dona',
            name='dataset_asociado',
            field=models.CharField(choices=[('sisa_letalidad_por_rango_etario', 'sisa_letalidad_por_rango_etario'), ('sisa_confirmados_por_rango_etario', 'sisa_confirmados_por_rango_etario'), ('sisa_positivos_por_dia', 'sisa_positivos_por_dia'), ('sisa_total_por_rango_etario', 'sisa_total_por_rango_etario'), ('sisa_positivos_alta_dia', 'sisa_positivos_alta_dia'), ('sisa_fallecidos_dia', 'sisa_fallecidos_dia'), ('sisa_positivos_genero', 'sisa_positivos_genero'), ('sisa_fallecidos_genero', 'sisa_fallecidos_genero'), ('sisa_fallecidos_promedio', 'sisa_fallecidos_promedio'), ('sisa_letalidad', 'sisa_letalidad'), ('sisa_positivos_acumulado', 'sisa_positivos_acumulado'), ('sisa_altas_acumulado', 'sisa_altas_acumulado'), ('sisa_fallecidos_acumulado', 'sisa_fallecidos_acumulado'), ('sisa_hisopados_totales_por_dia', 'sisa_hisopados_totales_por_dia'), ('sisa_hisopados_fecha', 'sisa_hisopados_fecha'), ('sisa_hisopados_totales_acumulado', 'sisa_hisopados_totales_acumulado'), ('sisa_hisopados_positivos_acumulado', 'sisa_hisopados_positivos_acumulado'), ('ufus_atencion_por_dia', 'ufus_atencion_por_dia'), ('repatriados_por_pais', 'repatriados_por_pais'), ('repatriados_por_pais_acumulado', 'repatriados_por_pais_acumulado'), ('botitriage_contactos_evolucion', 'botitriage_contactos_evolucion'), ('botitriage_contactos_acumulado', 'botitriage_contactos_acumulado'), ('llamados_107', 'llamados_107'), ('hospedados_ingresos_dia', 'hospedados_ingresos_dia'), ('hospedados_egresos_dia', 'hospedados_egresos_dia'), ('hospedados_acumulados', 'hospedados_acumulados'), ('hospedados_flujo', 'hospedados_flujo'), ('sube_ffcc_variacion_dia', 'sube_ffcc_variacion_dia'), ('sube_colectivo_variacion_dia', 'sube_colectivo_variacion_dia'), ('sube_subte_variacion_dia', 'sube_subte_variacion_dia'), ('sube_transporte_publico_evolucion', 'sube_transporte_publico_evolucion'), ('vehiculos_variacion_egreso_dia', 'vehiculos_variacion_egreso_dia'), ('vehiculos_variacion_ingreso_dia', 'vehiculos_variacion_ingreso_dia'), ('vehiculos_variacion_interna_dia', 'vehiculos_variacion_interna_dia'), ('vehiculos_variacion_ultimo_mes', 'vehiculos_variacion_ultimo_mes')], max_length=256, verbose_name='Dataset Asociado'),
        ),
        migrations.AlterField(
            model_name='grafico_cartesiano',
            name='dataset_asociado',
            field=models.CharField(choices=[('sisa_letalidad_por_rango_etario', 'sisa_letalidad_por_rango_etario'), ('sisa_confirmados_por_rango_etario', 'sisa_confirmados_por_rango_etario'), ('sisa_positivos_por_dia', 'sisa_positivos_por_dia'), ('sisa_total_por_rango_etario', 'sisa_total_por_rango_etario'), ('sisa_positivos_alta_dia', 'sisa_positivos_alta_dia'), ('sisa_fallecidos_dia', 'sisa_fallecidos_dia'), ('sisa_positivos_genero', 'sisa_positivos_genero'), ('sisa_fallecidos_genero', 'sisa_fallecidos_genero'), ('sisa_fallecidos_promedio', 'sisa_fallecidos_promedio'), ('sisa_letalidad', 'sisa_letalidad'), ('sisa_positivos_acumulado', 'sisa_positivos_acumulado'), ('sisa_altas_acumulado', 'sisa_altas_acumulado'), ('sisa_fallecidos_acumulado', 'sisa_fallecidos_acumulado'), ('sisa_hisopados_totales_por_dia', 'sisa_hisopados_totales_por_dia'), ('sisa_hisopados_fecha', 'sisa_hisopados_fecha'), ('sisa_hisopados_totales_acumulado', 'sisa_hisopados_totales_acumulado'), ('sisa_hisopados_positivos_acumulado', 'sisa_hisopados_positivos_acumulado'), ('ufus_atencion_por_dia', 'ufus_atencion_por_dia'), ('repatriados_por_pais', 'repatriados_por_pais'), ('repatriados_por_pais_acumulado', 'repatriados_por_pais_acumulado'), ('botitriage_contactos_evolucion', 'botitriage_contactos_evolucion'), ('botitriage_contactos_acumulado', 'botitriage_contactos_acumulado'), ('llamados_107', 'llamados_107'), ('hospedados_ingresos_dia', 'hospedados_ingresos_dia'), ('hospedados_egresos_dia', 'hospedados_egresos_dia'), ('hospedados_acumulados', 'hospedados_acumulados'), ('hospedados_flujo', 'hospedados_flujo'), ('sube_ffcc_variacion_dia', 'sube_ffcc_variacion_dia'), ('sube_colectivo_variacion_dia', 'sube_colectivo_variacion_dia'), ('sube_subte_variacion_dia', 'sube_subte_variacion_dia'), ('sube_transporte_publico_evolucion', 'sube_transporte_publico_evolucion'), ('vehiculos_variacion_egreso_dia', 'vehiculos_variacion_egreso_dia'), ('vehiculos_variacion_ingreso_dia', 'vehiculos_variacion_ingreso_dia'), ('vehiculos_variacion_interna_dia', 'vehiculos_variacion_interna_dia'), ('vehiculos_variacion_ultimo_mes', 'vehiculos_variacion_ultimo_mes')], max_length=256, verbose_name='Dataset Asociado'),
        ),
        migrations.AlterField(
            model_name='indicador',
            name='dataset_asociado',
            field=models.CharField(choices=[('sisa_letalidad_por_rango_etario', 'sisa_letalidad_por_rango_etario'), ('sisa_confirmados_por_rango_etario', 'sisa_confirmados_por_rango_etario'), ('sisa_positivos_por_dia', 'sisa_positivos_por_dia'), ('sisa_total_por_rango_etario', 'sisa_total_por_rango_etario'), ('sisa_positivos_alta_dia', 'sisa_positivos_alta_dia'), ('sisa_fallecidos_dia', 'sisa_fallecidos_dia'), ('sisa_positivos_genero', 'sisa_positivos_genero'), ('sisa_fallecidos_genero', 'sisa_fallecidos_genero'), ('sisa_fallecidos_promedio', 'sisa_fallecidos_promedio'), ('sisa_letalidad', 'sisa_letalidad'), ('sisa_positivos_acumulado', 'sisa_positivos_acumulado'), ('sisa_altas_acumulado', 'sisa_altas_acumulado'), ('sisa_fallecidos_acumulado', 'sisa_fallecidos_acumulado'), ('sisa_hisopados_totales_por_dia', 'sisa_hisopados_totales_por_dia'), ('sisa_hisopados_fecha', 'sisa_hisopados_fecha'), ('sisa_hisopados_totales_acumulado', 'sisa_hisopados_totales_acumulado'), ('sisa_hisopados_positivos_acumulado', 'sisa_hisopados_positivos_acumulado'), ('ufus_atencion_por_dia', 'ufus_atencion_por_dia'), ('repatriados_por_pais', 'repatriados_por_pais'), ('repatriados_por_pais_acumulado', 'repatriados_por_pais_acumulado'), ('botitriage_contactos_evolucion', 'botitriage_contactos_evolucion'), ('botitriage_contactos_acumulado', 'botitriage_contactos_acumulado'), ('llamados_107', 'llamados_107'), ('hospedados_ingresos_dia', 'hospedados_ingresos_dia'), ('hospedados_egresos_dia', 'hospedados_egresos_dia'), ('hospedados_acumulados', 'hospedados_acumulados'), ('hospedados_flujo', 'hospedados_flujo'), ('sube_ffcc_variacion_dia', 'sube_ffcc_variacion_dia'), ('sube_colectivo_variacion_dia', 'sube_colectivo_variacion_dia'), ('sube_subte_variacion_dia', 'sube_subte_variacion_dia'), ('sube_transporte_publico_evolucion', 'sube_transporte_publico_evolucion'), ('vehiculos_variacion_egreso_dia', 'vehiculos_variacion_egreso_dia'), ('vehiculos_variacion_ingreso_dia', 'vehiculos_variacion_ingreso_dia'), ('vehiculos_variacion_interna_dia', 'vehiculos_variacion_interna_dia'), ('vehiculos_variacion_ultimo_mes', 'vehiculos_variacion_ultimo_mes')], max_length=256, verbose_name='Dataset Asociado'),
        ),
        migrations.AlterField(
            model_name='tarjeta',
            name='dataset_asociado',
            field=models.CharField(choices=[('sisa_letalidad_por_rango_etario', 'sisa_letalidad_por_rango_etario'), ('sisa_confirmados_por_rango_etario', 'sisa_confirmados_por_rango_etario'), ('sisa_positivos_por_dia', 'sisa_positivos_por_dia'), ('sisa_total_por_rango_etario', 'sisa_total_por_rango_etario'), ('sisa_positivos_alta_dia', 'sisa_positivos_alta_dia'), ('sisa_fallecidos_dia', 'sisa_fallecidos_dia'), ('sisa_positivos_genero', 'sisa_positivos_genero'), ('sisa_fallecidos_genero', 'sisa_fallecidos_genero'), ('sisa_fallecidos_promedio', 'sisa_fallecidos_promedio'), ('sisa_letalidad', 'sisa_letalidad'), ('sisa_positivos_acumulado', 'sisa_positivos_acumulado'), ('sisa_altas_acumulado', 'sisa_altas_acumulado'), ('sisa_fallecidos_acumulado', 'sisa_fallecidos_acumulado'), ('sisa_hisopados_totales_por_dia', 'sisa_hisopados_totales_por_dia'), ('sisa_hisopados_fecha', 'sisa_hisopados_fecha'), ('sisa_hisopados_totales_acumulado', 'sisa_hisopados_totales_acumulado'), ('sisa_hisopados_positivos_acumulado', 'sisa_hisopados_positivos_acumulado'), ('ufus_atencion_por_dia', 'ufus_atencion_por_dia'), ('repatriados_por_pais', 'repatriados_por_pais'), ('repatriados_por_pais_acumulado', 'repatriados_por_pais_acumulado'), ('botitriage_contactos_evolucion', 'botitriage_contactos_evolucion'), ('botitriage_contactos_acumulado', 'botitriage_contactos_acumulado'), ('llamados_107', 'llamados_107'), ('hospedados_ingresos_dia', 'hospedados_ingresos_dia'), ('hospedados_egresos_dia', 'hospedados_egresos_dia'), ('hospedados_acumulados', 'hospedados_acumulados'), ('hospedados_flujo', 'hospedados_flujo'), ('sube_ffcc_variacion_dia', 'sube_ffcc_variacion_dia'), ('sube_colectivo_variacion_dia', 'sube_colectivo_variacion_dia'), ('sube_subte_variacion_dia', 'sube_subte_variacion_dia'), ('sube_transporte_publico_evolucion', 'sube_transporte_publico_evolucion'), ('vehiculos_variacion_egreso_dia', 'vehiculos_variacion_egreso_dia'), ('vehiculos_variacion_ingreso_dia', 'vehiculos_variacion_ingreso_dia'), ('vehiculos_variacion_interna_dia', 'vehiculos_variacion_interna_dia'), ('vehiculos_variacion_ultimo_mes', 'vehiculos_variacion_ultimo_mes')], max_length=256, verbose_name='Dataset Asociado'),
        ),
    ]
