FROM node:22.8.0-alpine3.20 AS build


RUN mkdir -p /var/www/dockerize-nuxt/nuxt-app
WORKDIR /var/www/dockerize-nuxt/nuxt-app

RUN apk add --update \
    curl
COPY package*.json ./
COPY . .
RUN rm yarn.lock
RUN yarn install 
RUN yarn run build

# FROM node:22.8.0-alpine3.20 AS production

RUN adduser --disabled-password nuxt --no-create-home
RUN chown -R nuxt:nuxt /var/www/dockerize-nuxt/nuxt-app
USER nuxt


EXPOSE 3000

CMD [ "yarn", "dev" ]