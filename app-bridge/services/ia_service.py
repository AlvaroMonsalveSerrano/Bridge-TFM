"""
El módulo ia_service.py define las funciones de servicio para realizar las 
operaciones de IA.
"""
import logging
import constant.constant_ia as cia
import helper.csv_helper as csvh
import exceptions.exceptions as excp

def do_ia_service(temperature: str, humidity:str) -> str:
    """
    La función do_ia_service realiza las operaciones de validación sobre los parámetros
    de temperatura y humedad.

    :param temperature: str -> Valor de temperatura.
    :param humidity: str -> Valor de humedad.

    :return str -> '0', si no hayuna situación de riesgo; 1, en otro caso.

    """
    logging.info(f"[**] /do_ia_service. temperatura='{temperature}' humedad='{humidity}'.")

    result = '0'
    temp_aux: float = verify_temperature(temperature)
    logging.info(f"[**] /do_ia_service. temperatura {temp_aux}.")

    humidity_aux: float = verify_humidity(humidity)
    logging.info(f"[**] /do_ia_service. humedad {humidity_aux}.")

    result = rule_safety(temp_aux, humidity_aux)
    logging.info(f"[**] /do_ia_service. resultado {result}.")

    return result

def find_temperature() -> str:
    """
    La función find_temperature() realiza la lectura del último valor de la temperatura
    registrado.
    """
    try:
        result = '0'
        logging.info(f"[**] /find_temperature.")
        result = csvh.find_temperature_old_value()
        logging.info(f"[**] /find_temperature: result={result}.")

        return result

    except Exception as ex:
        raise excp.ServiceException("Error en busqueda de la lectura de temperatura.")

def find_humidity() -> str:
    """
    La función find_humidity() realiza la lectura del último valor de la humedad.
    registrado.
    """
    try:
        result = '0'
        logging.info(f"[**] /find_humidity.")
        result = csvh.find_humidity_old_value()
        logging.info(f"[**] /find_humidity: result={result}.")

        return result

    except Exception as ex:
        raise excp.ServiceException("Error en busqueda de la lectura de humedad.")


def verify_temperature(temperature: str) -> float:
    try:
        result: float = 0
        logging.info(f"[**] /verify_temperature. Temperatura='{temperature}' {temperature == None} - {len(temperature)==0}.")
        if(temperature == None or len(temperature)==0 ): 
            result = float(csvh.find_temperature_old_value())
            logging.info(f"[**] /verify_temperature 1. result='{result}'.")
        else:    
            csvh.save_new_temperature(temperature)
            result = float(temperature)
            logging.info(f"[**] /verify_temperature 2. result='{result}'.")

        return result

    except Exception as ex:
        raise excp.ServiceException("Error en la verificación de temperatura")


def verify_humidity(humidity:str) -> float:
    try:
        result: float = 0
        logging.info(f"[**] /verify_humidity. Humedad='{humidity}'.")
        if(humidity == None or len(humidity)==0):  
            result = csvh.find_humidity_old_value()
            logging.info(f"[**] /verify_humidity 1. result='{result}'.")

        else:    
            csvh.save_new_humidity(humidity)
            result = float(humidity)
            logging.info(f"[**] /verify_humidity 2. result='{result}'.")
        

        return result
    
    except Exception as ex:
        raise excp.ServiceException("Error en la verificación de humedad")


def rule_safety(temperature: float, humidity: float) -> str:
    """
    La función rule_safety define la regla de negocio para determinar el 
    límite de los valores seguros.
    Los parámetros deben de ser válidos: no núlos.

    :return str -> 0, si no hay riesgo; 1, en otro caso.
    """
    result = '0'    
    if temperature >= cia.LIMIT_TEMPERATURE and humidity >= cia.LIMIT_HUMIDITY:
        result = '1'

    return result