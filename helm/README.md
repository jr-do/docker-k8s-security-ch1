# Helm Charts

This repo ships an umbrella chart with two subcharts: backend and frontend.

## Install
```bash
kubectl create namespace app-ch1
helm dependency update ./helm
helm install ch1 ./helm -n app-ch1
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
