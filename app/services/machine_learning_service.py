
# """
# El módulo machine_learning_service.py define las operaciones de negocio para las operaciones de 
# Machine Learning.
# """

# import os
# import logging
# import csv
# import pandas as pd
# import tensorflow as tf 

# from tensorflow import keras

# import helper.csv_helper as csvHelper
# import helper.configuration_parser_helper as configHelper
# import constant.constant_machine_learning as cml
# from constant.constant_union_trans import COLUMNS_CSV_METRICS_GOLD_ML
# import component.model_machine_learning as modelML
# import exceptions.machine_learning_exception as bde

# def create_ml_model() -> None:
#     """
#     La función create_ml_model define la funcionalidad para realizar la
#     creación del modelo de inteligencia.
    
#     :raise -> MachineLearningException
#     """

#     try:
#         dataset_path = __load_path_file_data__()
#         logging.info(f"[**] /create_ml_model: PATH cargado.{dataset_path}")

#         #
#         # 1.- CARGA DE DATOS
#         #
#         raw_dataset: pd.DataFrame = pd.read_csv(dataset_path, names=COLUMNS_CSV_METRICS_GOLD_ML)

#         logging.info(f"[**] /create_ml_model: raw_dataset.{raw_dataset}")

#         dataset:pd.DataFrame = raw_dataset.copy()

#         # print()
#         # print("# type(raw_dataset):\n", type(raw_dataset))
#         # print("# type(dataset):\n", type(dataset))
#         # print("# Dataset:\n", dataset)
#         logging.info(f"[**] /create_ml_model: carga de datos OK.")

#         #
#         # 2.- LIMPIEZA DE DATOS
#         #
#         # Eliminación de campos nulos.
#         dataset = dataset.dropna()
#         logging.info(f"[**] /create_ml_model: limpieza de datos OK.")

#         #
#         # 3.- CREACIÓN DE CONJUNTO DE DATOS DE ENTRENAMIENTO Y PRUEBAS.
#         #
#         train_dataset = dataset.sample(frac=0.8,random_state=0)
#         test_dataset = dataset.drop(train_dataset.index)
#         logging.info(f"[**] /create_ml_model: creación de datos de entrenamiento y pruebas OK.")

#         # print()
#         # print("# train_dataset:\n",train_dataset.tail())
#         # print("# test_dataset:\n",test_dataset.tail())

#         #
#         # 4.- NORMALIZACIÓN DE LOS DATOS
#         #

#         # Obtenemos las estadísticas para normalizar el modelo
#         train_stats = train_dataset.describe()
#         train_stats.pop(cml.COLUMN_NAME_FLAG)
#         train_stats = train_stats.transpose()

#         # Separamos el valor objetivo o etiqueta a calcular de las características. Tomamos toda la columna
#         train_labels: pd.Series = train_dataset.pop(cml.COLUMN_NAME_FLAG)
#         test_labels: pd.Series = test_dataset.pop(cml.COLUMN_NAME_FLAG)

#         # print()
#         # print("train_labels=", type(train_labels))
#         # print("test_labels=", type(test_labels)

#         print()
#         print("# train_dataset sin la columna etiqueta:\n",train_dataset.tail())
#         print("# test_dataset sin la columna etiqueta:\n",test_dataset.tail())

#         # Función de normalización.
#         # def myNormalize(x):
#         #     return (x - train_stats['mean']) / train_stats['std']

#         print("# train_stats:\n",train_stats) # OJO!!! NO HAY MEDIA PPUEDE QUE NO HAYA QUE NORMALIZAR!!!!

#         # normed_train_data: pd.DataFrame = myNormalize(train_dataset, train_stats)
#         # normed_test_data: pd.DataFrame = myNormalize(test_dataset, train_stats)      

#         # normed_train_data: pd.DataFrame = myNormalize(train_dataset)
#         # normed_test_data: pd.DataFrame = myNormalize(test_dataset)      

#         logging.info(f"[**] /create_ml_model: normalización de datos OK.")
#         print(f'longitud dataset: {len(train_dataset.keys())}')

#         mpgModel = modelML.MPGModel(len(train_dataset.keys()))

#         logging.info(f"[**] /create_ml_model: Modelo creado OK.")

#         #Entrenamiento
#         logging.info(f"[**] /create_ml_model: train_dataset: {type(train_dataset)}")
#         logging.info(f"[**] /create_ml_model: train_labels {type(train_labels)}")
#         modelo_entrenado = mpgModel.fit(train_dataset, train_labels, modelML.EPOCHS)

#         logging.info(f"[**] /create_ml_model: Modelo entrenado OK.")



#         logging.info(f"[**] /create_ml_model: modelo creado.")

#     except Exception as ex:
#         logging.error(f"[**] /create_ml_model...Error: {str(ex)}")
#         raise bde.MachineLearningException(str(ex))
    

# def myNormalize(x, train_stats):
#     return (x - train_stats['mean']) / train_stats['std']
            
# def __load_path_file_data__() -> str:
#     """
#     La función __load_path_file_data__ realiza la carga del PATH del fichero 
#     de datos para la creación del modelo.

#     :return str -> Path del fichero de datos.
#     """

#     filename: str = configHelper.PATH_GOLD_METRICS + "/"+ configHelper.FILENAME_METRICS_GOLD
#     logging.info(f"[***] /__load_filename_metrics__: filename metrics, {filename}.")

#     return filename    