# CD Deployment (Argo CD + Sealed Secrets)

This repo uses Argo CD (auto-sync) to deploy the Helm chart in `helm/`.

## Install Argo CD (namespace: ch1-exercise)
```bash
kubectl create namespace ch1-exercise
kubectl apply -n ch1-exercise -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

## Install Sealed Secrets (namespace: ch1-exercise)
```bash
kubectl apply -n ch1-exercise -f https://github.com/bitnami-labs/sealed-secrets/releases/latest/download/controller.yaml
```

## Add repo credentials to Argo CD
This repo is private, so Argo CD needs credentials to read it. You can add a repo using the Argo CD CLI:
```bash
argocd login <ARGOCD_SERVER>
argocd repo add https://github.com/jr-do/docker-k8s-security-ch1.git \
  --username jr-do \
  --password <GITHUB_PAT>
```

## Apply the Argo CD Application
```bash
kubectl apply -f deploy/argocd/ch1-application.yaml
```

## Sealed Secret for GHCR
Create a SealedSecret for the image pull secret and commit it under `deploy/sealed-secrets/`.
See `deploy/sealed-secrets/README.md`.
