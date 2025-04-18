#!/bin/sh
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
	CREATE USER citizen WITH SUPERUSER PASSWORD '${POSTGRES_PASSWORD}';
	CREATE DATABASE civo OWNER citizen;
	GRANT ALL PRIVILEGES ON DATABASE civo TO citizen;
EOSQL