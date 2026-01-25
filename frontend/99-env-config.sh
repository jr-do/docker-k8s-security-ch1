#!/usr/bin/env sh
set -eu

: "${API_BASE_URL:=http://localhost:8080}"

envsubst < /usr/share/nginx/html/config.template.js > /usr/share/nginx/html/config.js
