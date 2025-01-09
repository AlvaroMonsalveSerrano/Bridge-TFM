
import logging

import constant.constant_oxygen as cteOxigeno
import constant.constant_temperature as cteTemperature
import constant.constant_humedad as cteHumidity
import constant.constant_union_trans as cteTransform

import helper.csv_helper as csvHelper

import exceptions.transform_exception as te

def transform_metric_data() -> None:
    """
    La función transform_metric_data define la funcionalidad para realizar la
    transformación de los datos de las métricas inyectadas en ficheros CSV para 
    la unificación en una única fuente.
    
    :raise -> TransformException
    """

    try:
        filename_oxygen, filename_temperature, filename_humidity, filename_transform = __load_filename_metrics__()
        logging.info(f"[**] /transform_metric_data: ficheros cargados.")

        csvHelper.create_file_union_metrics(filename_oxygen, filename_temperature, filename_humidity, filename_transform)
        logging.info(f"[**] /transform_metric_data: union creada.")

    except Exception as ex:
        logging.error(f"[**] /transform_metric_data...Error: {str(ex)}")
        raise te.TransformException(str(ex))


def __load_filename_metrics__():
    """
    La función __load_filename_metrics__ realiza la carga de los path de los ficheros CSV 
    a cargar.

    :return -> Path del fichero oxigeno.
    :return -> Path del fichero temperatura. 
    :return -> Path del fichero humedad.

    """

    filename_oxygen = cteOxigeno.PATH_OXYGEN_METRICS + "/"+ cteOxigeno.FILENAME_METRICS_OXYGEN_RAW
    logging.info(f"[***] /__load_filename_metrics__: filename_oxygen, {filename_oxygen}.")
    
    filename_temperature = cteTemperature.PATH_TEMPERATURE_METRICS + "/"+ cteTemperature.FILENAME_METRICS_TEMPERATURE_RAW
    logging.info(f"[***] /__load_filename_metrics__: filename_temperature, {filename_temperature}.")

    filename_humidity = cteHumidity.PATH_HUMIDITY_METRICS + "/" + cteHumidity.FILENAME_METRICS_HUMIDITY_RAW
    logging.info(f"[***] /__load_filename_metrics__: filename_humidity, {filename_humidity}.")

    filename_transform = cteTransform.PATH_TRANS_METRICS + "/" + cteTransform.FILENAME_METRICS_TRANS
    logging.info(f"[***] /__load_filename_metrics__: filename_transform, {filename_transform}.")

    return filename_oxygen, filename_temperature, filename_humidity, filename_transform

def transform_to_gold_data() -> None:
    """
    La función transform_to_gold_data define la funcionalidad para realizar la
    transformación de los datos de las métricas para su almacenamiento en un 
    lago de datos.
    
    :raise -> TransformException
    """

    try:
        filename_transform, filename_gold = __load_transform_metrics__()
        logging.info(f"[**] /transform_to_gold_data: ficheros cargados.")

        csvHelper.create_file_gold(filename_transform, filename_gold)
        logging.info(f"[**] /transform_to_gold_data: insertado en DataLake.")

    except Exception as ex:
        logging.error(f"[**] /transform_to_gold_data...Error: {str(ex)}")
        raise te.TransformException(str(ex))


def __load_transform_metrics__():
    """
    La función __load_transform_metrics__ realiza la carga del path del fichero CSV 
    con las transformaciones de datos.

    :return -> Path del fichero transformación.

    """
    filename_transform = cteTransform.PATH_TRANS_METRICS + "/" + cteTransform.FILENAME_METRICS_TRANS
    logging.info(f"[***] /__load_transform_metrics__: filename_transform, {filename_transform}.")

    filename_gold = cteTransform.PATH_GOLD_METRICS + "/" + cteTransform.FILENAME_METRICS_GOLD
    logging.info(f"[***] /__load_transform_metrics__: filename_gold, {filename_gold}.")

    return filename_transform, filename_gold
