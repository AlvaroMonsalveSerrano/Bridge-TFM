
"""
El módulo bigdata_service.py define las operaciones de negocio 
"""

import os
import logging
import csv
import influxdb_client

from influxdb import InfluxDBClient
from influxdb.resultset import ResultSet

import constant.constant_oxygen as cteOxigeno
import constant.constant_temperature as cteTemperature
import constant.constant_humedad as cteHumidity

import helper.csv_helper as csvHelper
import helper.configuration_parser_helper as configHelper

import exceptions.bigdata_exception as bde


def read_data_from_bridge() -> None:
    """
    La función read_data_from_bridge define la funcionalidad de la lectura de las 
    mediciones de InfluxDB.
    :raise -> BigDataException
    """

    HOST = configHelper.INFLUXDB_HOST
    PORT = configHelper.INFLUXDB_PORT
    DATABASE_INFLUX = configHelper.INFLUXDB_DATABASE_NAME

    try:
        client = InfluxDBClient(host=HOST, port=PORT)
        logging.info(f"[**] /read_data_from_bridge: cliente creado.")

        client.switch_database(DATABASE_INFLUX)
        logging.info(f"[**] /read_data_from_bridge: seleccionada base de datos.")

        # Oxigeno.
        resultOxygen: ResultSet = client.query(cteOxigeno.QUERY_OXYGEN)
        logging.info(f"[**] /read_data_from_bridge: {cteOxigeno.QUERY_OXYGEN}")
        oxygen_points = list(resultOxygen.get_points(measurement=cteOxigeno.METRIC_NAME_OXYGEN))
        csvHelper.create_oxygen_raw(oxygen_points)

        # Temperatura.
        resultTemperature: ResultSet = client.query(cteTemperature.QUERY_TEMPERATURE)
        logging.info(f"[**] /read_data_from_bridge: {cteTemperature.QUERY_TEMPERATURE}")
        temperature_points = list(resultTemperature.get_points(measurement=cteTemperature.METRIC_NAME_TEMPERATURE))
        csvHelper.create_temperature_raw(temperature_points)

        # Humedad
        resultHumidity: ResultSet = client.query(cteHumidity.QUERY_HUMIDITY)
        logging.info(f"[**] /read_data_from_bridge: {cteHumidity.QUERY_HUMIDITY}")
        humidity_points = list(resultHumidity.get_points(measurement=cteHumidity.METRIC_NAME_HUMIDITY))
        csvHelper.create_humidity_raw(humidity_points)


    except Exception as ex:
        logging.error(f"[**] /read_data_from_bridge...Error: {str(ex)}")
        raise bde.BigDataException(str(ex))

    finally:
        client.close()
        logging.info(f"[**] /read_data_from_bridge: conexión cliente BBDD cerrado.")
