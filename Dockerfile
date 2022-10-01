FROM docker.io/python:3.9-slim

RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		build-essential \
		libpq-dev \
		postgresql-client \
		python3-dev \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

RUN make db
RUN make load

EXPOSE 8000
CMD ["python", "plebiscito_root/manage.py", "runserver", "0.0.0.0:8000"]
