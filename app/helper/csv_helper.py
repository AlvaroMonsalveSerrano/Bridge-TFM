
import logging
import csv

import constant.constant_oxygen as cteOxigeno
from exceptions.helper_exception import CsvHelperException

def create_oxygen_raw(lstOxigeno: list) -> None:
    """
    La función create_origeno_raw realiza la creación del fichero Csv con los datos
    en crudo de las métricas pasadas por parámetro. 
    """

    assert (lstOxigeno != None or len(lstOxigeno) >= 0), f"Lista de métricas de oxígeno no valida."

    try:
        with open(f'{cteOxigeno.PATH_OXIGENO_METRICS}/{cteOxigeno.FILE_METRICS_OXYGEN_RAW}', mode='w') as file:
            writer = csv.DictWriter(file, delimiter=',', fieldnames=cteOxigeno.COLUMNS_CSV_METRICS)
            writer.writeheader()
            for point in lstOxigeno:
                writer.writerow(point)  
        logging.info(f"[***] /create_oxygen_raw: fichero oxigeno_raw.csv creado. ")

    except Exception as ex:
        raise CsvHelperException(str(ex))



    