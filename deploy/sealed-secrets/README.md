# Sealed Secrets

This folder is for SealedSecrets (e.g., GHCR pull credentials).

## Create the GHCR pull secret (plaintext YAML)
```bash
kubectl -n app-ch1 create secret docker-registry ghcr-pull \
  --docker-server=ghcr.io \
  --docker-username=jr-do \
  --docker-password=<GHCR_TOKEN> \
  --dry-run=client -o yaml > ghcr-pull.yaml
```

## Seal it
```bash
kubeseal -n app-ch1 -o yaml < ghcr-pull.yaml > ghcr-pull.sealed.yaml
```

Commit `ghcr-pull.sealed.yaml` into this folder.
