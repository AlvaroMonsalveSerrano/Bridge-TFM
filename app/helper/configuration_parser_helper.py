from configparser import ConfigParser
import constant.constant_properties as cteProperties

parser = ConfigParser()
parser.read(cteProperties.PATH_FILE_INI_PROPERTIES)

INFLUXDB_HOST = parser.get('INFLUXDB', 'HOST')
INFLUXDB_PORT = parser.get('INFLUXDB', 'PORT')
INFLUXDB_DATABASE_NAME = parser.get('INFLUXDB', 'NAME_DATABASE_INFLUX')

PATH_OXYGEN_METRICS = parser.get('OXYGEN_METRICS','PATH_OXYGEN_METRICS')
FILENAME_METRICS_OXYGEN_RAW = parser.get('OXYGEN_METRICS','FILENAME_METRICS_OXYGEN_RAW')

