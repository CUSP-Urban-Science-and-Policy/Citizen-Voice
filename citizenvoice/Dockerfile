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
    zlib-dev
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

RUN adduser --disabled-password --no-create-home django
COPY . .
RUN chown -R django:django /var/www/dockerize-django/citizenvoice
USER django

# COPY wait-for-it.sh /wait-for-it.sh
# RUN chmod +x /wait-for-it.sh

# ENV DJANGO_ALLOWED_HOSTS=localhost

# EXPOSE 8000

# CMD [ "/wait-for-it.sh", "db-postgis:5432", "--", "python", "manage.py", "runserver", "0.0.0.0:8000" ]
# CMD ["uwsig", "--socket", ":8000", "--workers", "4", "--master", "--enable-threads", "--module", "citizenvoice.wsgi"]
