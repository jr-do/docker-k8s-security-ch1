# Helm Charts

This repo ships an umbrella chart with two subcharts: backend and frontend.

## Install
```bash
kubectl create namespace app-ch1
kubectl -n app-ch1 create secret docker-registry ghcr-pull \
  --docker-server=ghcr.io \
  --docker-username=jr-do \
  --docker-password=<GHCR_TOKEN>
helm dependency update ./helm
helm install ch1 ./helm -n app-ch1 \
  --set backend.imagePullSecrets[0]=ghcr-pull \
  --set frontend.imagePullSecrets[0]=ghcr-pull
```

## Upgrade
```bash
helm upgrade ch1 ./helm -n app-ch1
```

## Uninstall
```bash
helm uninstall ch1 -n app-ch1
```

## Values
Default images are set to GHCR and can be overridden.

Example override:
```bash
helm upgrade --install ch1 ./helm -n app-ch1 \
  --set backend.image.tag=latest \
  --set frontend.image.tag=latest
```

By default, the frontend Service is a NodePort on `30080`.
