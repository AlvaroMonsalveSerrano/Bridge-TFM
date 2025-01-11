#
# Makefile. Definición del fichero makefile para trabajar exclusivamente con el app 
# Python utilizando Python.
#


##  ==========================================
##  =============   APP PYTHON   =============
##  ==========================================
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



##  ========================================================
##  =============   APP OPERACIÓN CON DOCKER   =============
##  ========================================================
.PHONY: build
build:
	docker image build -t alvaroms/tfm-app-bridge:v1.1 .

.PHONY: run
run:
	docker container run -d --name tfm-local-bridge -p 6060:80 --env FILE_CONFIG_PATH=/app -v /home/alvaro/data-bridge:/data alvaroms/tfm-app-bridge:v1.1

.PHONY: exec
exec:
	docker container exec -it tfm-local-bridge /bin/sh

.PHONY: logs
logs:
	docker container logs tfm-local-bridge

.PHONY: stopc
stopc:
	docker container stop tfm-local-bridge

.PHONY: rmc
rmc:
	docker container rm tfm-local-bridge

.PHONY: all
all:  build run