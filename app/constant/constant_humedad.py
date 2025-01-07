"""
Definición de las constantes para la operación de la métrica temperatura.
"""
import helper.configuration_parser_helper as configHelper

#
# CONSULTAS DE NEGOCIO
# 
QUERY_HUMIDITY = 'SELECT * FROM humedad'
METRIC_NAME_HUMIDITY = 'humedad'

#
# CONSTANTES DE PROCESAMIENTO
#
COLUMNS_CSV_METRICS_HUMIDITY = ['time', 'value']
PATH_HUMIDITY_METRICS = configHelper.PATH_HUMIDITY_METRICS
FILENAME_METRICS_HUMIDITY_RAW = configHelper.FILENAME_METRICS_HUMIDITY_RAW
