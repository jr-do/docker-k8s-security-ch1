FROM nginx:1.27-alpine

COPY index.html /usr/share/nginx/html/index.html
COPY config.template.js /usr/share/nginx/html/config.template.js
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY 99-env-config.sh /docker-entrypoint.d/99-env-config.sh

RUN chmod +x /docker-entrypoint.d/99-env-config.sh

EXPOSE 80
