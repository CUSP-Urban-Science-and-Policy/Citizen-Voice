#!/bin/bash

set -e

echo "Checking for dhparam.pem"
if [ ! -f "/vol/proxy/ssl-dhparam.pem" ]; then
  echo "Generating dhparam.pem"
  openssl dhparam -out /vol/proxy/ssl-dhparam.pem 4096 # path must match the one in the default-ss.conf.tpl
fi

# avoid replacing these with envsubst
export host=\$host
export request_uri=\$request_uri

echo "Checking for fullchain.pem"
if [ ! -f "/etc/letsencrypt/life/${DOMAIN}/fullchain.pem" ]; then
  echo "No SSL certificate, enabling HTTP only..."
  envsubst < /etc/nginx/default.conf.tpl > /etc/nginx/conf.d/default.conf
else
    echo "SSL certificate found, enabling HTTPS..."
    envsubst < /etc/nginx/default-ssl.conf.tpl > /etc/nginx/conf.d/default.conf
fi

nginx -g 'daemon off;'
