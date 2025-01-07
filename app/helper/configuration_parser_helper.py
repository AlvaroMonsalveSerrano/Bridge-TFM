from configparser import ConfigParser
import constant.constant_properties as cteProperties

parser = ConfigParser()
#parser.read('/home/alvaro/Documentos/Master-IOT/TFM/Prototipo/app/properties/configuration.ini')
parser.read(cteProperties.PATH_FILE_INI_PROPERTIES)

INFLUXDB_HOST = parser.get('INFLUXDB', 'HOST')
INFLUXDB_PORT = parser.get('INFLUXDB', 'PORT')
INFLUXDB_DATABASE_NAME = parser.get('INFLUXDB', 'NAME_DATABASE_INFLUX')

