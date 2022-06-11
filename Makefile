PWD 				:= src
DB_NAME 			:= $(shell echo mydatabase)
DB_PATH				:= $(CURDIR)/${DB_NAME}

FIXTURE_ARRAY := $(shell ls plebiscito_root/*/fixture/*.yaml)

.PHONY: db db-clean db-reload load test dev

dev: 
	python $(PWD)/manage.py runserver

db: 
	python3 ${PWD}/manage.py makemigrations
	python3 ${PWD}/manage.py migrate

load:
	@for fixture in ${FIXTURE_ARRAY}; do \
		echo Loading $$fixture ; \
		python3 ${PWD}/manage.py loaddata $$fixture ; \
	done

db-reload: db-clean db load

check-clean: 
	@echo -n "¿Seguro? [y/N] " && read ans && [ $${ans:-N} = y ]
	@echo Confirmado

db-clean: check-clean
ifeq (,$(wildcard ${DB_PATH}))
	@[ -e "${DB_PATH}" ] && rm ${DB_PATH} && echo "DB eliminada: ${DB_PATH}" || echo "${DB_PATH} no existe"
else
	@echo "DB no existe"
	@echo ${DB_NAME"}
endif

compose:
	docker-compose up

compose_rebuild:
	docker-compose build && docker-compose up 

help-install:
	@echo "python3 -m venv .venv"
	@echo "source .venv/bin/activate"
	@echo "which python # Deberia apuntar a Python3"
	@echo "pip install -r requirements.txt"
