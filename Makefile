PWD 					:= ./plebiscito_root
DB_NAME 			:= db.sqlite3
FIXTURE_ARRAY := $(shell ls plebiscito_root/*/fixture/*.yaml)

.PHONY: db db_clean load db_reload test

db:
	python3 ${PWD}/manage.py makemigrations
	python3 ${PWD}/manage.py migrate

db_clean:
	rm ${PWD}/${DB_NAME}

load:
	@for fixture in ${FIXTURE_ARRAY}; do \
		echo Loading $$fixture ; \
		python3 ${PWD}/manage.py loaddata $$fixture ; \
	done

db_reload: db_clean db load

compose:
	docker-compose up

compose_rebuild:
	docker-compose build && docker-compose up 
