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

server {
    listen 443 ssl;
    server_name ${DOMAIN} www.${DOMAIN};
    
    ssl_certificate /etc/letsencryt/live/${DOMAIN}/fullchain.pem;
    ssl_certificate_key /etc/letsencryt/live/${DOMAIN}/privkey.pem;

    include /etc/nginx/options-ssl-nginx.conf;
    ssl_dhparam /vol/proxy/ssl-dhparams.pem;

    add_header Strict-Transport-Security "max-age=315600; includeSubDomains" always;

    location /static {
        alias /vol/static;
    }

    location / {
        uwsgi_pass              ${APP_HOST}:${APP_PORT};
        include                 /etc/nginx/uwsgi_params;
        client_max_body_size    10M;
    }
}