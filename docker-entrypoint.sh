#!/bin/bash

# Collect static files
echo "Collect static files"
python /opt/plebiscito/plebiscito_root/manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python /opt/plebiscito/plebiscito_root/manage.py migrate

echo "Populate database with fixtures"
for fixture in `ls plebiscito_root/*/fixture/*.yaml`; do
  python ${PWD}/plebiscito_root/manage.py loaddata $fixture
done 

# Start server
echo "Starting server"
python /opt/plebiscito/plebiscito_root/manage.py runserver 0.0.0.0:8000
