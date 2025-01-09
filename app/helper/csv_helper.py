
import logging
import csv

import constant.constant_oxygen as cteOxigeno
import constant.constant_temperature as cteTemperature
import constant.constant_humedad as cteHumidity
import constant.constant_union_trans as cteTransform

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
    
    finally:
        file.close()

    
def create_file_union_metrics(filename_oxygen: str, 
                              filename_temperature: str,
                              filename_humidity: str,
                              filename_transform: str) -> None:
    """
    El método create_file_union_metrics realiza la creación de un fichero CSV unificado
    con las métricas de los ficheros pasados por parámetros.

    :param -> filename_oxygen, path de las métricas de oxigeno.
    :param -> filename_temperature, path de las métricas de temperatura.
    :param -> filename_humidity, path de las métricas de humedad.
    :param -> filename_transform, path del fichero de transformación.

    :raise -> CsvHelperException 

    :return -> None
    """    

    assert (filename_oxygen != None or len(filename_oxygen) >= 0), f"Path del fichero csv oxigeno no válido."
    assert (filename_temperature != None or len(filename_temperature) >= 0), f"Path del fichero csv temperatura no válido."
    assert (filename_humidity != None or len(filename_humidity) >= 0), f"Path del fichero csv humedad no válido."
    assert (filename_transform != None or len(filename_transform) >= 0), f"Path del fichero csv transformación no válido."

    try:
        with open(filename_oxygen, 'r') as f_oxy, \
             open(filename_temperature, 'r') as f_temp, \
             open(filename_humidity, 'r') as f_hum, \
             open(filename_transform, 'w') as f_trans:
            
            writer = csv.writer(f_trans) 

            for csv_oxyg, csv_temp, csv_hum in zip(csv.reader(f_oxy), csv.reader(f_temp), csv.reader(f_hum)):
                writer.writerow( (*csv_oxyg, *csv_temp, *csv_hum) )

            logging.info(f"[**] /create_file_union_metrics: Ficheros transfromación creados.")


    except Exception as ex:
        raise CsvHelperException(str(ex))
    
    finally:
        f_oxy.close()
        f_temp.close()
        f_hum.close()
        f_trans.close()


def create_file_gold(filename_transform: str, 
                     filename_gold: str) -> None:
    """
    El método create_file_union_metrics realiza la creación de un fichero CSV unificado
    con las métricas de los ficheros pasados por parámetros.

    :param -> filename_transform, path de las métricas.
    :param -> filename_gold, path del fichero gold.

    :raise -> CsvHelperException 

    :return -> None
    """    

    assert (filename_transform != None or len(filename_transform) >= 0), f"Path del fichero csv transformación no válido."
    assert (filename_gold != None or len(filename_gold) >= 0), f"Path del fichero csv gold no válido."

    try:
        headers_gold = cteTransform.COLUMNS_CSV_METRICS_GOLD
        with open(filename_transform, 'r') as f_trans, \
             open(filename_gold, 'w') as f_gold:

            csv_gold = csv.writer(f_gold)
            csv_gold.writerow(headers_gold)

            csv_transform = csv.reader(f_trans)
            next(csv_transform)
            for row in csv_transform:
                time_oxy, value_oxy, time_temp, value_temp, time_hum, value_hum, *_= row
                row = [time_oxy, value_oxy, value_temp, value_hum, __flag_ia_model__(value_temp, value_hum)]
                csv_gold.writerow(row)

        logging.info(f"[**] /create_file_gold: Fichero gold creado.")


    except Exception as ex:
        raise CsvHelperException(str(ex))
    
    finally:
        f_trans.close()
        f_gold.close()


def __flag_ia_model__(value_temp:str, value_hum:str) -> int:
    """
    La función __flag_ia_model__ define la regla para determinar si una situación medida
    en una situación real supone una situación crítica.

    :param value_temp -> Valor de temperatura.
    :param value_hum  -> Valor de humedad.  
    """
    try:
        temperature = float(value_temp)
        humidity = float(value_hum)
        result = 0

        if temperature >= 100.0 and humidity >= 70.0:
            result = 1

        return result
    
    except Exception as ex:
        raise ex

