"""
Definición de las constantes para la operación de transformación.
"""
import helper.configuration_parser_helper as configHelper

#
# CONSTANTES DE PROCESAMIENTO
#
COLUMNS_CSV_METRICS_TEMPERATURE = ['time', 'oxigeno', 'temperatura', 'humedad', 'flag']
PATH_TRANS_METRICS = configHelper.PATH_TRANS_METRICS
FILENAME_METRICS_TRANS = configHelper.FILENAME_METRICS_TRANS


COLUMNS_CSV_METRICS_GOLD_ML = ['oxigeno', 'temperatura', 'humedad', 'flag']
COLUMNS_CSV_METRICS_GOLD = ['oxigeno', 'temperatura', 'humedad', 'flag']
PATH_GOLD_METRICS = configHelper.PATH_GOLD_METRICS
FILENAME_METRICS_GOLD = configHelper.FILENAME_METRICS_GOLD

