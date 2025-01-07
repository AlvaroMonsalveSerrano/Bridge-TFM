"""
Definición de las constantes para la operación de la métrica oxígeno.
"""
import helper.configuration_parser_helper as configHelper

#
# CONSULTAS DE NEGOCIO
# 
QUERY_OXYGEN = 'SELECT * FROM oxigeno'
METRIC_NAME_OXYGEN = 'oxigeno'

#
# CONSTANTES DE PROCESAMIENTO
#
COLUMNS_CSV_METRICS = ['time', 'value']
PATH_OXYGEN_METRICS = configHelper.PATH_OXYGEN_METRICS
FILENAME_METRICS_OXYGEN_RAW = configHelper.FILENAME_METRICS_OXYGEN_RAW
