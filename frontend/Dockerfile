FROM node:22.8.0-alpine3.20 AS build

# ENV NODE_ENV=production

WORKDIR /var/www/dockerize-nuxt/nuxt-app

COPY package*.json ./

RUN yarn install --fronzen-lockfile

COPY . .

RUN yarn run build

FROM node:22.8.0-alpine3.20 AS production

RUN mkdir -p /var/www/dockerize-nuxt/nuxt-app
WORKDIR /var/www/dockerize-nuxt/nuxt-app

RUN apk add --no-cache curl

COPY --from=build /var/www/dockerize-nuxt/nuxt-app /var/www/dockerize-nuxt/nuxt-app
RUN adduser --disabled-password nuxt && \
    chown -R nuxt:nuxt /var/www/dockerize-nuxt/nuxt-app

USER nuxt

EXPOSE 3000

CMD [ "yarn", "start" ]