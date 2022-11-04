FROM python:3.11-slim-bullseye

ENV PYTHONUNBUFFERED 1  
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt update -y && \
    apt upgrade -y && \
    apt install -y libpq-dev build-essential

WORKDIR /usr/app/

COPY requirements.txt ./

copy plebiscito_root /usr/app/src

RUN pip install --no-cache-dir -r requirements.txt

RUN python /usr/app/src/manage.py makemigrations

EXPOSE 8000

CMD ["python", "/usr/app/src/manage.py", "runserver", "localhost:8000"]