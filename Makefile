
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
.PHONY: build 
build:
	docker-compose -f infra-dc.yml -p miPrototipo build

.PHONY: up
up:
	docker-compose -f infra-dc.yml -p miPrototipo up -d

.PHONY: start
start:
	docker-compose -f infra-dc.yml -p miPrototipo start 

.PHONY: stop
stop:
	docker-compose -f infra-dc.yml -p miPrototipo stop 	

.PHONY: restart
restart:
	docker-compose -f infra-dc.yml -p miPrototipo stop 	
	docker-compose -f infra-dc.yml -p miPrototipo up -d

# Borra solo los contenedores, no borra los volúmenes.
.PHONY: down
down:
	docker-compose -f infra-dc.yml -p miPrototipo down 

# Borrar los volumenes de datos.
.PHONY: destroy
destroy:
	docker-compose -f infra-dc.yml -p miPrototipo down -v 	

.PHONY: ps
ps:
	docker-compose -f infra-dc.yml -p miPrototipo ps  	

.PHONY: logs
logs:
	docker-compose -f infra-dc.yml -p miPrototipo logs --tail=100 -f 

.PHONY: logs-nodered
logs-nodered:
	docker-compose -f infra-dc.yml -p miPrototipo logs --tail=100 -f nodered

.PHONY: logs-mosquitto
logs-mosquitto:
	docker-compose -f infra-dc.yml -p miPrototipo logs --tail=100 -f mosquitto

.PHONY: logs-influxDB
logs-influxDB:
	docker-compose -f infra-dc.yml -p miPrototipo logs --tail=100 -f influxDB	

.PHONY: logs-grafanaui
logs-grafanaui:
	docker-compose -f infra-dc.yml -p miPrototipo logs --tail=100 -f grafanaui	

.PHONY: logs-app-compose
logs-app-compose:
	docker-compose -f infra-dc.yml -p miPrototipo logs --tail=100 -f app		