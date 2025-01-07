
import logging
import csv

import constant.constant_oxygen as cteOxigeno
import constant.constact_temperature as cteTemperature
import constant.constant_humedad as cteHumidity

from exceptions.helper_exception import CsvHelperException

def create_oxygen_raw(lstOxigeno: list) -> None:
    """
    La función create_origeno_raw realiza la creación del fichero CSV con los datos
    en crudo de las métricas pasadas por parámetro. 
    
    :param -> lstOxigeno, lista de datos
    :raise -> CsvHelperException
    :return -> None
    """

    assert (lstOxigeno != None or len(lstOxigeno) >= 0), f"Lista de métricas de oxígeno no valida."

    try:
        __create_csv_file__(lst = lstOxigeno, 
                            path_file = cteOxigeno.PATH_OXYGEN_METRICS,
                            name_file = cteOxigeno.FILENAME_METRICS_OXYGEN_RAW,
                            columns_name = cteOxigeno.COLUMNS_CSV_METRICS    )

    except Exception as ex:
        raise CsvHelperException(str(ex))


def create_temperature_raw(lstTemperature: list) -> None:
    """
    La función create_temperature_raw realiza la creación del fichero CSV con los datos
    en crudo de las métricas pasadas por parámetro. 
    
    :param -> lstTemperature, lista de datos
    :raise -> CsvHelperException
    :return -> None
    """

    assert (lstTemperature != None or len(lstTemperature) >= 0), f"Lista de métricas de temperatura no valida."

    try:
        __create_csv_file__(lst = lstTemperature, 
                            path_file = cteTemperature.PATH_TEMPERATURE_METRICS,
                            name_file = cteTemperature.FILENAME_METRICS_TEMPERATURE_RAW,
                            columns_name = cteTemperature.COLUMNS_CSV_METRICS_TEMPERATURE )

    except Exception as ex:
        raise CsvHelperException(str(ex))


def create_humidity_raw(lstHumidity: list) -> None:
    """
    La función create_humidity_raw realiza la creación del fichero CSV con los datos
    en crudo de las métricas pasadas por parámetro. 
    
    :param -> lstHumidity, lista de datos
    :raise -> CsvHelperException
    :return -> None
    """

    assert (lstHumidity != None or len(lstHumidity) >= 0), f"Lista de métricas de humedad no valida."

    try:
        __create_csv_file__(lst = lstHumidity, 
                            path_file = cteHumidity.PATH_HUMIDITY_METRICS,
                            name_file = cteHumidity.FILENAME_METRICS_HUMIDITY_RAW,
                            columns_name = cteHumidity.COLUMNS_CSV_METRICS_HUMIDITY)

    except Exception as ex:
        raise CsvHelperException(str(ex))


def __create_csv_file__(lst: list, path_file: str, name_file: str, columns_name: list) -> None:
    """
    La función __create_csv_file__ realiza la creación de un fichero csv con los datos y condiciones
    pasados por parámetro.

    :param -> lst, lista de datos
    :param -> path_file, path del fichero CSV
    :param -> name_file, nombre del fichero CSV
    :param -> columns_name, nombre de las columnas del fichero CSV
    :raise -> Exception
    :return -> None
    """

    assert (lst != None or len(lst) >= 0), f"Lista de métricas de oxígeno no válida."
    assert (path_file != None or len(path_file) >= 0), f"Path del fichero csv no válido."
    assert (name_file != None or len(name_file) >= 0), f"Nombre del fichero csv no válido."
    assert (columns_name != None or len(columns_name) >= 0), f"Nombre de columnas csv no válido."

    try:
        with open(f'{path_file}/{name_file}', mode='w') as file:
            writer = csv.DictWriter(file, delimiter=',', fieldnames=columns_name)
            writer.writeheader()
            for point in lst:
                writer.writerow(point)  
        logging.info(f"[***] /__create_csv_file__: fichero {name_file} creado. ")

    except Exception as ex:
        raise ex

    