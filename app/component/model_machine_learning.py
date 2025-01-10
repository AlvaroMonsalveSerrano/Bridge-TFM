
# """
# El módulo model_machine_learning.py define los componentes para realizar el 
# modelo de machine learning.

# """

# import pandas as pd
# import tensorflow as tf
# from tensorflow import keras
# import logging

# EPOCHS:  int = 5

# class PrintDot(keras.callbacks.Callback):
#   '''
#   PrintDot clase de utilidad para la visualización de un caracter
#   por consola cuando se está entrenando el modelo.
#   '''

#   def on_epoch_end(self, epoch, logs):
#     if epoch % 100 == 0: print('')
#     print('.', end='')



# class MPGModel():
#     '''
#     MPGModel es un modelo de regresión básico para estimar el valor
#     MPG de un conjunto de autos.
#     '''

#     def __init__(self, len_dataset:int ) -> None:
#         '''
#         Constructor básico de la clase MPGModel.
#         '''

#         self.model = keras.Sequential([
#             keras.layers.Dense(64, activation='relu', input_shape=[len_dataset]),
#             keras.layers.Dense(64, activation='relu'),
#             keras.layers.Dense(1)
#         ])

#         self.optimizer = tf.keras.optimizers.RMSprop(0.001)

#         self.model.compile(
#             loss='mse',
#             optimizer=self.optimizer,
#             metrics=['mae','mse']
#         )


#     def fit(self, train_data: pd.DataFrame, train_labels: pd.Series, epochs_value:int):
#         '''
#         Función de entrenamiento del modelo.
#         '''
#         logging.info(f"[****] /fit START")
#         logging.info(f"[****] /fit {type(train_data)}")
#         logging.info(f"[****] /fit {type(train_labels)}")

#         print(f'TRAIN_DATA')
#         print(train_data)
#         print(f'TRAIN_LABEL')
#         print(train_labels)

#         try:
#             modelo_entrenado = self.model.fit(
#                 train_data, train_labels,
#                 epochs=epochs_value, validation_split=0.2, verbose=0,
#                 callbacks=[PrintDot()]
#             )
#         except Exception as ex:
#            print(f'Exception-> {ex}')

#         logging.info(f"[****] /fit END")

#         return modelo_entrenado
    

#     def evaluate(self, data: pd.DataFrame, labels: pd.Series):
#        '''
#        Función de evaluación del modelo.

#        Retorna los siguientes valores: loss, mae, mse
#        '''
#        loss, mae, mse = self.model.evaluate(data, labels, verbose=2) 

#        return loss, mae, mse
    
#     def predict(self, data: pd.DataFrame):
#        '''
#        Función de predicción del modelo.
#        '''

#        return self.model.predict(data)


#     def saveModel(self, path: str):
#        '''
#        Función almacena el modelo.
#        '''
#        return self.model.save(path)
