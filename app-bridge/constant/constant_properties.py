"""
Definición de las constantes de propiedades.
"""

import os
import logging

FILE_CONFIG_PATH = os.environ["FILE_CONFIG_PATH"]
logging.info(f"[] /constant_properties: FILE_CONFIG_PATH='{FILE_CONFIG_PATH}'.")
print(f"[] /constant_properties: FILE_CONFIG_PATH='{FILE_CONFIG_PATH}'.")


PATH_FILE_INI_PROPERTIES = FILE_CONFIG_PATH + '/configuration.ini'