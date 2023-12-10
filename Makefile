
# Evitamos la asociación del "comando typehint" por un fichero existente con el mismo nombre. 

##  =============
##  =============   APP PYTHON 
##  =============
.PHONY: create-venv
create-venv:
	virtualenv .venv -p python3
# source .venv/bin/activate

.PHONY: rm-venv
rm-venv:
	rm -rf .venv

.PHONY: install-library
install-library:
	pip3 install -r requirements.txt

#
# DOCKER APP
#
.PHONY: buildapp
buildapp:	
	docker image build -t alvaroms/tfm-app:v1.0 ./app

.PHONY: runapp
runapp:
	docker container run -d --name tfm-app -p 6060:80 alvaroms/tfm-app:v1.0

.PHONY: stopapp
stopapp:
	docker container stop tfm-app

.PHONY: rmapp
rmapp:
	docker container rm tfm-app	

.PHONY: execapp
execapp:
	docker container exec -it tfm-app /bin/sh

.PHONY: logs-app
logs-app:
	docker container logs tfm-app


##  =============
##  =============   DOCKER COMPOSE 
##  =============

## build
.PHONY: buildb
buildb:
	docker-compose -f infra-bridge.yml -p miPrototipoBridge build

.PHONY: buildp
buildp:
	docker-compose -f infra-platform.yml -p miPrototipoPlatform build


## UP
.PHONY: upp
upp:
	docker-compose -f infra-platform.yml -p miPrototipoPlatform up -d --force-recreate	

.PHONY: upb
upb:
	docker-compose -f infra-bridge.yml -p miPrototipoBridge up -d --force-recreate

.PHONY: upb-bbdd
upb-bbdd:
	docker exec influxDB influx -execute 'create database TFM'
	

## start
.PHONY: startb
startb:
	docker-compose -f infra-bridge.yml -p miPrototipoBridge start 

.PHONY: startp
startp:
	docker-compose -f infra-platform.yml -p miPrototipoPlatform start 


## stop
.PHONY: stopb
stopb:
	docker-compose -f infra-bridge.yml -p miPrototipoBridge stop 	

.PHONY: stopp
stopp:
	docker-compose -f infra-platform.yml -p miPrototipoPlatform stop


#restart
.PHONY: restartb
restartb:
	docker-compose -f infra-bridge.yml -p miPrototipoBridge stop 	
	docker-compose -f infra-bridge.yml -p miPrototipoBridge up -d

.PHONY: restartp
restartp:
	docker-compose -f infra-platform.yml -p miPrototipoPlatform stop 	
	docker-compose -f infra-platform.yml -p miPrototipoPlatform up -d	


# down
# Borra solo los contenedores, no borra los volúmenes.
.PHONY: downb
downb:
	docker-compose -f infra-bridge.yml -p miPrototipoBridge down 

# Borra solo los contenedores, no borra los volúmenes.
.PHONY: downp
downp:
	docker-compose -f infra-platform.yml -p miPrototipoPlatform down 	



# destroy
# Borrar los volumenes de datos.
.PHONY: destroyp
destroyp:
	docker-compose -f infra-platform.yml -p miPrototipoPlatform down -v 	

.PHONY: destroyb
destroyb:
	docker-compose -f infra-bridge.yml -p miPrototipoBridge down -v 



#ps
.PHONY: psp
psp:
	docker-compose -f infra-platform.yml -p miPrototipoPlatform ps  	

.PHONY: psb
psb:
	docker-compose -f infra-bridge.yml -p miPrototipoBridge ps  



#logs Bridge
.PHONY: logs-nodered
logs-nodered:
	docker-compose -f infra-bridge.yml -p miPrototipoBridge logs --tail=100 -f nodered


.PHONY: logs-mosquitto
logs-mosquitto:
	docker-compose -f infra-bridge.yml -p miPrototipoBridge logs --tail=100 -f mosquitto	


.PHONY: logs-influxDB
logs-influxDB:
	docker-compose -f infra-bridge.yml -p miPrototipoBridge logs --tail=100 -f influxDB	



# logs Platform
.PHONY: logs-grafanaui
logs-grafanaui:
	docker-compose -f infra-platform.yml -p miPrototipoPlatform logs --tail=100 -f grafanaui	

.PHONY: logs-app
logs-app:
	docker-compose -f infra-platform.yml -p miPrototipoPlatform logs --tail=100 -f app		