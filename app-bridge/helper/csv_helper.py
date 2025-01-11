"""
El módulo csv_helper define las operaciones sobre los ficheros csv.
"""
import logging
import helper.configuration_parser_helper as cph
import exceptions.exceptions as ex
import helper.configuration_parser_helper as cph

def find_temperature_old_value() -> str:
    """
    La función find_temperature_old_and_save realiza la obtención del último valor
    de la métrica temperatura.

    :return str
    """

    try:
        result = ''
        filename_temperature = cph.PATH_TEMPERATURE + "/" + cph.FILENAME_TEMPERATURE 
        logging.info(f"[***] /find_temperature_old_value. filename_temperature={filename_temperature}.")
        file = open(filename_temperature, 'r')
        result = file.readline()
        logging.info(f"[***] /find_temperature_old_value. result={result}.")

        return result
    
    except Exception as ex:
        raise str.HelperException(str(ex))
    finally:
        file.close()


def find_humidity_old_value() -> str:
    """
    La función find_humidity_old_value realiza la obtención del último valor
    de la métrica humedad.

    :return str
    """
    try:
        result = ''
        filename_humidity = cph.PATH_HUMIDITY + "/" + cph.FILENAME_HUMIDITY 
        logging.info(f"[***] /find_humidity_old_value. filename_humidity={filename_humidity}.")
        file = open(filename_humidity, 'r')
        result = file.readline()
        logging.info(f"[***] /find_humidity_old_value. result={result}.")

        return result
    
    except Exception as ex:
        raise str.HelperException(str(ex))
    finally:
        file.close()


def save_new_temperature(new_temperature: str) -> None:
    """
    La función save_new_temperature guarda el valor pasado por parámetro en un fichero.

    :param temperature:str -> Nuevo valor a almacenar.

    :return None.
    """
    try:
        filename_temperature = cph.PATH_TEMPERATURE + "/" + cph.FILENAME_TEMPERATURE 
        file = open(filename_temperature, 'w')
        file.write(new_temperature)
    
    except Exception as ex:
        raise str.HelperException(str(ex))
    finally:
        file.close()


def save_new_humidity(new_humidity: str) -> None:
    """
    La función save_new_humidity guarda el valor pasado por parámetro en un fichero.

    :param new_humidity:str -> Nuevo valor a almacenar.

    :return None.
    """
    try:
        filename_humidity = cph.PATH_HUMIDITY + "/" + cph.FILENAME_HUMIDITY 

        logging.info(f"[***] /save_new_humidity. filename_humidity={filename_humidity} new_humidity={new_humidity}.")

        file = open(filename_humidity, 'w')
        file.write(new_humidity)
    
    except Exception as ex:
        raise str.HelperException(str(ex))
    
    finally:
        file.close()
