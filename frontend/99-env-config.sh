#!/usr/bin/env sh
set -eu

if [ -z "${API_BASE_URL+x}" ]; then
  API_BASE_URL="http://localhost:8080"
fi

envsubst < /usr/share/nginx/html/config.template.js > /usr/share/nginx/html/config.js
