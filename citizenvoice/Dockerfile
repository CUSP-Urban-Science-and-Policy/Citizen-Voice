FROM python:3.11-alpine3.20

ENV PYTHONUNBUFFERED 1 \
    PYTHONDONTWRITEBYTECODE 1

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
    curl \
    libffi-dev

RUN pip install --upgrade pip

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /citizenvoice
COPY . /citizenvoice
RUN python manage.py collectstatic --no-input

RUN adduser --disabled-password --no-create-home django && \
    chown -R django:django /citizenvoice

USER django

EXPOSE 8000

