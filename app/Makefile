#
# Makefile. Definición del fichero makefile para trabajar exclusivamente con el app 
# Python utilizando Python.
#
.PHONY: build
build:
	docker image build -t alvaroms/tfm:v1.0 .

.PHONY: run
run:
	docker container run -d --name tfm-local -p 6060:80 --env IP_BRIDGE=192.168.1.158 alvaroms/tfm:v1.0

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