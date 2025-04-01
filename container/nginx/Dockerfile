FROM nginx:1.27.1-alpine3.20

COPY ./configs/* /etc/nginx/
COPY ./run.sh /run.sh

ENV APP_HOST=django-app
ENV APP_PORT=8000 

RUN apk add --no-cache openssl bash
RUN chmod +x /run.sh

VOLUME /vol/static
VOLUME /vol/www

CMD ["/run.sh"]

