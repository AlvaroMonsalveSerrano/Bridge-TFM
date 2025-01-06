
import os
import logging
import csv
import influxdb_client

from influxdb import InfluxDBClient

import exceptions.bigdata_exception as bde


# def read_data_from_bridge() -> None:
#     """
#     La función read_data_from_bridge define la funcionalidad de la lectura de las 
#     mediciones de InfluxDB.
#     """

#     URL = "http://192.168.1.158:8086"
#     BUCKET = "TFM"
#     ORG = ""
#     TOKEN = ""

#     try:
#         client = influxdb_client.InfluxDBClient(
#             url=URL,
#             token=TOKEN,
#             org=ORG
#         )
#         logging.info(f"[**] /read_data_from_bridge: cliente creado")
        
#         query_api = client.query_api()
#         logging.info(f"[**] /read_data_from_bridge: query_api creada")

#         query = f'from(bucket:"{BUCKET}")\
#             |> range(start: -10m)\
#             |> filter(fn:(r) => r._measurement == "my_measurement")\
#             |> filter(fn:(r) => r.location == "Prague")\
#             |> filter(fn:(r) => r._field == "temperature")'
#         logging.info(f"[**] /read_data_from_bridge: consulta creada")
        
#         result = query_api.query(org=ORG, query=query)
#         logging.info(f"[**] /read_data_from_bridge: consulta ejecutada")
#         results = []
#         for table in result:
#             for record in table.records:
#                 results.append((record.get_field(), record.get_value()))

#         print(results)

#     except Exception as ex:
#         logging.error(f"[**] /read_data_from_bridge...Error: {str(ex)}")
#         raise bde.BigDataException(str(ex))




def read_data_from_bridge() -> None:
    """
    La función read_data_from_bridge define la funcionalidad de la lectura de las 
    mediciones de InfluxDB.
    """

    HOST = "192.168.1.158"
    PORT = 8086
    DATABASE = 'TFM'
    QUERY = 'SELECT * FROM oxigeno'
    COLUMNS_CSV_METRICS = ['time', 'value']
    PATH_OXIGENO_METRICS = '/home/alvaro/Documentos/Master-IOT/TFM/Prototipo/csv'

    try:
        client = InfluxDBClient(host=HOST, port=PORT)
        logging.info(f"[**] /read_data_from_bridge: cliente creado.")

        client.switch_database(DATABASE)
        logging.info(f"[**] /read_data_from_bridge: seleccionada base de datos.")

        result = client.query(QUERY)
        logging.info(f"[**] /read_data_from_bridge: {QUERY}")

        logging.info(f"[**] /read_data_from_bridge: type(result)={type(result)}")
        # logging.info(f"[**] /read_data_from_bridge: result={result}")

        oxigeno_points = list(result.get_points(measurement='oxigeno'))
        logging.info(f"[**] /read_data_from_bridge: oxigeno_points={oxigeno_points}")

        for point in oxigeno_points:
            print(f'Point={point}')

        with open(f'{PATH_OXIGENO_METRICS}/oxigeno.csv', mode='w') as file:
            writer = csv.DictWriter(file, delimiter=',', fieldnames=COLUMNS_CSV_METRICS)
            writer.writeheader()
            for point in oxigeno_points:
                writer.writerow(point)           
            

    except Exception as ex:
        logging.error(f"[**] /read_data_from_bridge...Error: {str(ex)}")
        raise bde.BigDataException(str(ex))

    finally:
        client.close()
        logging.info(f"[**] /read_data_from_bridge: DDBB cerrada.")
