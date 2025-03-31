FROM node:22.8.0-alpine3.20


RUN mkdir -p /var/www/dockerize-nuxt/nuxt-app
WORKDIR /var/www/dockerize-nuxt/nuxt-app

RUN apk add --update \
    curl
RUN adduser --disabled-password nuxt
COPY package*.json ./
COPY . .
RUN rm yarn.lock
RUN chown -R nuxt:nuxt /var/www/dockerize-nuxt/nuxt-app
USER nuxt


RUN yarn install 
# RUN yarn run build

EXPOSE 3000

CMD [ "yarn", "dev" ]