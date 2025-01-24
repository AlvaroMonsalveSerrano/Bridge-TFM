"""
API REST para el módulo de IA a instalar en el dispositivo en el borde.
To run application:

1.-
    >cd entrypoints/
    >export FLASK_APP=app.py
    >flask run

2.-
    >FLASK_APP=app.py flask run

To test application:

    >curl http://localhost:5000/
"""

import uuid
import logging

from flask import Flask, jsonify, request, current_app

import services.ia_service as ias

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)


@app.route("/", methods=['GET'])
def root():
    """
    Root entrypoint
    :return: str
    """
    current_app.logger.info(f"[*] /root")
    return jsonify({'result': 'Ok'}), 200


@app.route("/liveness", methods=['GET'])
def liveness():
    """
    Liveness entrypoint.
    :return: str
    """
    current_app.logger.info(f"[*] /liveness")
    return 'Ok', 200


@app.route("/readiness", methods=['GET'])
def rediness():
    """
    Rediness entrypoint.
    :return: str
    """
    current_app.logger.info(f"[*] /rediness")
    return 'Ok', 200

"""
curl "http://localhost:5000/ia?temperatura=10&humedad=20"
curl "http://localhost:5000/ia?temperatura=60&humedad=40"
curl "http://localhost:5000/ia?temperatura=61&humedad=41"
"""
@app.route("/ia", methods=['GET'])
def ia():
    """
    IA entrypoint.
    :return: str. '0' no hay riesgo; '1', si hay riesgo.
    """

    try:
        result = '0'
        temperature = request.args.get('temperatura')
        humidity = request.args.get('humedad')
        current_app.logger.info(f"[*] /ia. Parámetros: temperatura={temperature} humedad={humidity}")

        result = ias.do_ia_service(temperature, humidity)
        current_app.logger.info(f"[*] /ia. result: {result}")

    except Exception as ex:
        current_app.logger.info(f"[*] /ia. Exception: {str(ex)}")

    return result, 200

@app.route("/ia2", methods=['GET'])
def ia2():
    """
    IA entrypoint.
    :return: str. '0' no hay riesgo; '1', si hay riesgo.
    """

    try:
        result = '0'
        temperature = request.args.get('temperatura')
        humidity = request.args.get('humedad')
        current_app.logger.info(f"[*] /ia. Parámetros: temperatura={temperature} humedad={humidity}")

        result = ias.do_ia_service(temperature, humidity)
        current_app.logger.info(f"[*] /ia. result: {result}")

    except Exception as ex:
        current_app.logger.info(f"[*] /ia. Exception: {str(ex)}")

    return jsonify({'result': result}), 200

@app.route("/iatemperature", methods=['GET'])
def iatemperature():
    try:
        result = '0'
        current_app.logger.info(f"[*] /iatemperature.")
        result = ias.find_temperature()
        current_app.logger.info(f"[*] /iatemperature. Result: {result}")

    except Exception as ex:
        current_app.logger.info(f"[*] /iatemperature. Exception: {str(ex)}")

    return result, 200

@app.route("/iatemperature2", methods=['GET'])
def iatemperature2():
    try:
        result = '0'
        current_app.logger.info(f"[*] /iatemperature.")
        result = ias.find_temperature()
        current_app.logger.info(f"[*] /iatemperature. Result: {result}")

    except Exception as ex:
        current_app.logger.info(f"[*] /iatemperature. Exception: {str(ex)}")

    return jsonify({'result': result}), 200

@app.route("/iahumidity", methods=['GET'])
def iahumidity():
    try:
        result = '0'
        current_app.logger.info(f"[*] /iahumidity.")
        result = ias.find_humidity()
        current_app.logger.info(f"[*] /iahumidity. Result: {result}")

    except Exception as ex:
        current_app.logger.info(f"[*] /iahumidity. Exception: {str(ex)}")

    return result, 200

@app.route("/iahumidity2", methods=['GET'])
def iahumidity2():
    try:
        result = '0'
        current_app.logger.info(f"[*] /iahumidity.")
        result = ias.find_humidity()
        current_app.logger.info(f"[*] /iahumidity. Result: {result}")

    except Exception as ex:
        current_app.logger.info(f"[*] /iahumidity. Exception: {str(ex)}")

    return jsonify({'result': result}), 200

if __name__ == '__main__':
    app.run(debug=True)