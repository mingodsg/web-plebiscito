PWD := ./plebiscito_root
DB_NAME := db.sqlite3

db:
	python3 ${PWD}/manage.py makemigrations
	python3 ${PWD}/manage.py migrate

db_clean:
	rm ${PWD}/${DB_NAME}

load:
	python3 ${PWD}/manage.py loaddata plebiscito_root/polls/fixture/init-Question.yaml
	python3 ${PWD}/manage.py loaddata plebiscito_root/polls/fixture/init-Choice.yaml

db_reload: db_clean db load
