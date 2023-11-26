#
# Makefile. Definición del fichero makefile para trabajar exclusivamente con el app 
# Python utilizando Python.
#
.PHONY: build
build:
	docker image build -t alvaroms/tfm:v1.0 .

.PHONY: run
run:
	docker container run -d --name tfm-local -p 6060:80 alvaroms/tfm:v1.0

.PHONY: exec
exec:
	docker container exec -it tfm-local /bin/sh

.PHONY: logs
logs:
	docker container logs tfm-local


.PHONY: all
all:  build run