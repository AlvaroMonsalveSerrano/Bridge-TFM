
import logging
import csv

import constant.constant_oxygen as cteOxigeno
from exceptions.helper_exception import CsvHelperException

def create_oxygen_raw(lstOxigeno: list) -> None:
    """
    La función create_origeno_raw realiza la creación del fichero Csv con los datos
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
        with open(f'{cteOxigeno.PATH_OXYGEN_METRICS}/{cteOxigeno.FILENAME_METRICS_OXYGEN_RAW}', mode='w') as file:
            writer = csv.DictWriter(file, delimiter=',', fieldnames=cteOxigeno.COLUMNS_CSV_METRICS)
            writer.writeheader()
            for point in lst:
                writer.writerow(point)  
        logging.info(f"[***] /__create_csv_file__: fichero oxigeno_raw.csv creado. ")

    except Exception as ex:
        raise ex

    