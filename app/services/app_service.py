
import logging
import paho.mqtt.client as mqtt

from exceptions.services_exception import ServiceException

#
broker_address = "localhost"
topic_alarm1 = "app/binomio1/alarm1"
topic_alarm2 = "app/binomio1/alarm2"
topic_alarm3 = "app/binomio1/alarm3"

def send_message_to_broker_mqtt(topic: str, message: str, alarm_type:str) -> None:
    """
    La función send_message_to_broker_mqtt define la funcionalidad del envío de un 
    mensaje al borket MQTT
    """

    assert (topic != None and len(topic) > 0), f"Nombre topic no valido"
    assert (message != None and len(message)>0), f"Mensaje no valido"
    assert (alarm_type != None and len(alarm_type)>0), f"Tipo de alarma no valido"

    client = mqtt.Client('Client MQTT') # Creación del cliente
    logging.info(f"[**] /app_service. Cliente MQTT creado")   

    client.connect(broker_address)
    logging.info(f"[**] /app_service. Conectado al broker MQTT...")

    client.publish(topic, message)
    client.disconnect()
    logging.info(f"[**] /app_service. Mensaje alarma {alarm_type} publicado.")
    


def setAlarm1() -> None:
    """
    La función setAlarm1 es aquella alarma que envía la alarma de tipo 1 al broker MQTT.

    :return: None
    """

    try:
        message_alarm1 = "ON1"
        type_alarm = "Alarm1"
        send_message_to_broker_mqtt(topic_alarm1, message_alarm1, type_alarm )   # 
        logging.info(f"[**] /app_service. Fin {type_alarm}.")

    except AssertionError as ex:
        raise ServiceException(str(ex))


def setAlarm2() -> None:
    """
    La función setAlarm2 es aquella alarma que envía la alarma de tipo 2 al broker MQTT.

    :return: None
    """

    message_alarm1 = "ON2"
    type_alarm = "Alarm2"
    send_message_to_broker_mqtt(topic_alarm2, message_alarm1, type_alarm )
    logging.info(f"[**] /app_service. Fin setAlarm {type_alarm}.")


def setAlarm3() -> None:
    """
    La función setAlarm3 es aquella alarma que envía la alarma de tipo 3 al broker MQTT.

    :return: None
    """

    message_alarm = "ON3"
    type_alarm = "Alarm3"
    send_message_to_broker_mqtt(topic_alarm3, message_alarm, type_alarm )
    logging.info(f"[**] /app_service. Fin setAlarm {type_alarm}.")