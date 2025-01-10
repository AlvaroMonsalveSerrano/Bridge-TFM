
FROM python:3.8-alpine

RUN apk add --no-cache --virtual .build-deps gcc musl-dev python3-dev
RUN apk add libpq

COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

RUN apk del --no-cache .build-deps

RUN mkdir -p /data
RUN mkdir -p /app
COPY . /app/
# COPY ./properties/configuration_docker.ini /app/configuration.ini
WORKDIR /app
ENV FLASK_APP=entrypoints/app.py FLASK_DEBUG=1 PYTHONUNBUFFERED=1 FILE_CONFIG_PATH=.
CMD flask run --host=0.0.0.0 --port=80
