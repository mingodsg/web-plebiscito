PLEBISCITO
----------------------- 
python3.8
python3.8-venv
------------------------

Plataforma de consultas populares.

DB consta de tres tablas:
	- Publicaciones
	- Votos (pk=Publicaciones)
	- Usuarios (pk=Publicaciones/votos)

Los usuarios podrán:
	- Crear publicaciones
	- Votar sólo una vez en cada publicación
	- Buscar publicaciones

TO DO:

- MODELS:
	- Question (DONE)
	- Choice (DONE)
	- User 

- TEMPLATES:
	- PREGUNTAS:
		- Detail (DONE Basic) 
		- Results (DONE Basic) 
		- Index (DONE Basic) (Home, User dashboard, search results)
		- Crear pregunta
	- USUARIOS:
		- Users login
		- Users signup

# Instalación

## OS
Además de tener los paquetes de Python3 y pip, algunas librerías son necesarias:
* `libpq-dev` (en Debian/Ubuntu) para poder correr pg_config (Dependencia de PostgreSQL)
* `wheel` 
