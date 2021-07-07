FROM python:3
# Needed for non buffering
# https://stackoverflow.com/questions/59812009/what-is-the-use-of-pythonunbuffered-in-docker-file#59812588 
ENV PYTHONUNBUFFERED=1
WORKDIR /opt/plebiscito
COPY requirements.txt /opt/plebiscito
ADD . /opt/plebiscito
RUN pip install -r requirements.txt
EXPOSE 8000
# CMD ["python", "/opt/plebiscito/plebiscito_root/manage.py", "runserver", "0.0.0.0:8000"]
ENTRYPOINT ["/opt/plebiscito/docker-entrypoint.sh"]
