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
	docker image build -t alvaroms/tfm:v2.0 .

.PHONY: run
run:
	docker container run -d --name tfm-local -p 6060:80 --env IP_BRIDGE=192.168.1.158  -v /home/alvaro/data_csv:/data alvaroms/tfm:v2.0

.PHONY: exec
exec:
	docker container exec -it tfm-local /bin/sh

.PHONY: logs
logs:
	docker container logs tfm-local

.PHONY: stopc
stopc:
	docker container stop tfm-local

.PHONY: rmc
rmc:
	docker container rm tfm-local

.PHONY: all
all:  build run