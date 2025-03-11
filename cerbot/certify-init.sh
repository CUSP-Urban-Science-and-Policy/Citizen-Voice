#!/bin/sh

# Wait for proxy to be available, then gets the first certificate

set -e

until nc -z proxy 80; do
  echo "Waiting for proxy to be available..."
  sleep 5 & wait ${!}
done

echo "Getting certificate for ${DOMAIN}"

certbot certonly \
    --webroot \
    --webroot-path "/vol/www/" \  
    -d "${DOMAIN}" \
    --email "${EMAIL}" \
    --rsa-key-size 4096 \
    --agree-tos \
    --noninteractive

