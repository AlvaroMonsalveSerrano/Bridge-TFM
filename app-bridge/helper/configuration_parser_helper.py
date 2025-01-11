from configparser import ConfigParser
import constant.constant_properties as cteProperties
import logging

parser = ConfigParser()
parser.read(cteProperties.PATH_FILE_INI_PROPERTIES)

logging.info(f"[] /configuration_parser_helper. Path properties='{cteProperties.PATH_FILE_INI_PROPERTIES}'.")

PATH_TEMPERATURE = parser.get('TEMPERATURE_METRICS','PATH_TEMPERATURE')
FILENAME_TEMPERATURE = parser.get('TEMPERATURE_METRICS','FILENAME_TEMPERATURE')


PATH_HUMIDITY = parser.get('HUMIDITY_METRICS','PATH_HUMIDITY')
FILENAME_HUMIDITY = parser.get('HUMIDITY_METRICS','FILENAME_HUMIDITY')

