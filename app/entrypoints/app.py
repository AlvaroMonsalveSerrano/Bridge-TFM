"""
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
from services import app_service 
from exceptions.services_exception import ServiceException


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


@app.route("/alarm1", methods=['GET'])
def doAlarm1():
    """
    Alarm1 entrypoint
    :return: str, código error. (510- Error de servicio de negocio)
    """

    response_result = None
    code_result = 0
    try:
        current_app.logger.info(f"[*] /alarm1")
        app_service.setAlarm1()
        response_result = {'result': 'Ok'}
        code_result = 200
    
    except ServiceException as service_exception:
        response_result = {'result': 'Ko', 'error': str(service_exception)}
        code_result = 510        

    return jsonify(response_result), code_result


@app.route("/alarm2", methods=['GET'])
def doAlarm2():
    """
    Alarm1 entrypoint
    :return: str
    """

    response_result = None
    code_result = 0
    try:

        current_app.logger.info(f"[*] /alarm2")
        app_service.setAlarm2()
        response_result = {'result': 'Ok'}
        code_result = 200

    except ServiceException as service_exception:
        response_result = {'result': 'Ko', 'error': str(service_exception)}
        code_result = 510        

    return jsonify(response_result), code_result


@app.route("/alarm3", methods=['GET'])
def doAlarm3():
    """
    Alarm3 entrypoint
    :return: str
    """

    response_result = None
    code_result = 0
    try:

        current_app.logger.info(f"[*] /alarm3")
        app_service.setAlarm3()
        response_result = {'result': 'Ok'}
        code_result = 200

    except ServiceException as service_exception:
        response_result = {'result': 'Ko', 'error': str(service_exception)}
        code_result = 510        

    return jsonify(response_result), code_result

if __name__ == '__main__':
    app.run(debug=True)