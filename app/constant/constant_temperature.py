"""
Definición de las constantes para la operación de la métrica temperatura.
"""
import helper.configuration_parser_helper as configHelper

#
# CONSULTAS DE NEGOCIO
# 
QUERY_TEMPERATURE = 'SELECT * FROM temperatura'
METRIC_NAME_TEMPERATURE = 'temperatura'

#
# CONSTANTES DE PROCESAMIENTO
#
COLUMNS_CSV_METRICS_TEMPERATURE = ['time', 'value']
PATH_TEMPERATURE_METRICS = configHelper.PATH_TEMPERATURE_METRICS
FILENAME_METRICS_TEMPERATURE_RAW = configHelper.FILENAME_METRICS_TEMPERATURE_RAW
