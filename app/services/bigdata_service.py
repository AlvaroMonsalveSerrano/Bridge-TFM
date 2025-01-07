
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
import helper.csv_helper as csvHelper
import helper.configuration_parser_helper as configHelper

import exceptions.bigdata_exception as bde


def read_data_from_bridge() -> None:
    """
    La función read_data_from_bridge define la funcionalidad de la lectura de las 
    mediciones de InfluxDB.
    """

    HOST = configHelper.INFLUXDB_HOST
    PORT = configHelper.INFLUXDB_PORT
    DATABASE_INFLUX = configHelper.INFLUXDB_DATABASE_NAME

    try:
        client = InfluxDBClient(host=HOST, port=PORT)
        logging.info(f"[**] /read_data_from_bridge: cliente creado.")

        client.switch_database(DATABASE_INFLUX)
        logging.info(f"[**] /read_data_from_bridge: seleccionada base de datos.")

        result: ResultSet = client.query(cteOxigeno.QUERY)
        logging.info(f"[**] /read_data_from_bridge: {cteOxigeno.QUERY}")

        oxygen_points = list(result.get_points(measurement=cteOxigeno.METRIC_NAME_OXYGEN))
        csvHelper.create_oxygen_raw(oxygen_points)

    except Exception as ex:
        logging.error(f"[**] /read_data_from_bridge...Error: {str(ex)}")
        raise bde.BigDataException(str(ex))

    finally:
        client.close()
        logging.info(f"[**] /read_data_from_bridge: conexión cliente BBDD cerrado.")
