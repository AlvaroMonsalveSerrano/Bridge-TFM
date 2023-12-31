
# APP

## Introducción

Aplicación para el envío de mensajes a la placa controladora a travéx del Broker MQTT Mosquitto

## Creación entorno de desarrollo

    1.- Creación del entorno virtual.
      1.1.- Creación del entorno: $>virtualenv -p python3.6 .venv
      1.2.- Activar el entorno: $>source .venv/bin/activate
      1.3.- Para desactivar el entorno: $>desactivate
    
      El entorno virtual se instala en la carpeta .venv del proyecto.
    
    2.- Instalación d elas dependencias: $>pip install -r requirements.txt  

## Test

```
pytest --setup-show
```


## Run

Hay dos formas de arrancar la aplicación, en las dos formas, hay que ubicarse en la carpeta del proyecto:

1.- Definiendo una variable de entorno de forma explicita:
```
cd entrypoints/
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

2.- Definiendo la variable de entorno de forma implícita.
```
cd entrypoints/
FLASK_ENV=development FLASK_DEBUG=0 FLASK_APP=app.py flask run
```

Para probar los endpoint:

```
curl http://localhost:5000/
curl http://localhost:5000/readiness
curl http://localhost:5000/liveness
curl http://127.0.0.1:6060/alarm1
curl http://127.0.0.1:6060/alarm2
curl http://127.0.0.1:6060/alarm3
```

## Docker 

1.- Creación de la imagen. Operación **build** del fichero Makefile.
``` 
docker image build -t alvaroms/tfm:v1.0

>make build
```

2.- Arrancar el contenedor. Operación **run** del fichero Makefile.
``` 
docker container run -d --name tfm-app -p 6060:80 alvaroms/tfm:v1.0

>make run
```

3.- Entrar en la consola del contenedor. Operación **exec** del fichero Makefile.
``` 
docker container exec -it tfm-app /bin/sh

>make exec
```

4.- Visualizar los logs del contenedor. Operación **logs** del fichero Makefile.
``` 
docker container logs tfm-app

> make logs
```

5.- Para la ejecución conjunto de las operaciones básicas: test, creación de la imagen y arranque
se emplea el comando **all** del fichero Makefile.

```
>make all
```

Para probar los endpoints de la aplicación arrancada en el contenedor, se pueden utilizar los siguientes comandos curl:

```
curl http://localhost:6060/
curl http://localhost:6060/liveness
curl http://localhost:6060/rediness
```

