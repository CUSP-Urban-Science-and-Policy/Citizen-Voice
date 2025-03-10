FROM python:3.11-alpine3.20

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir -p /var/www/dockerize-django/citizenvoice
WORKDIR /var/www/dockerize-django/citizenvoice

COPY ./requirements.txt ./
# packages required for building GDAL
RUN apk add --no-cache \
    python3-dev \
    gdal \
    gdal-dev \
    gcc \
    musl-dev \
    geos-dev \
    proj-dev \
    postgresql-dev \
    build-base \
    libjpeg-turbo-dev \
    zlib-dev \
    curl
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

RUN adduser --disabled-password --no-create-home django
COPY . .
RUN python manage.py collectstatic --no-input
RUN chown -R django:django /var/www/dockerize-django/citizenvoice
USER django
