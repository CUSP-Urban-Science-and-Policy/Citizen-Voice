server {
    listen 80;
    server_name ${DOMAIN} www.${DOMAIN};

    location /.well-knon/acme-challenge/ {
        root /vol/www/;
    }

    location / {
        return 301 https://$host$request_uri;
    }
}