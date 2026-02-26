# podman-api

A simple Flask API containerized with Podman

## Prerequisites
- Tested on macOS with Podman version 5.8.0 installed via HomeBrew

## Build
```bash
podman build -t myimage .
```

## Run
```bash
podman run --rm --name mycontainer -p 8000:8000 myimage
```

## Quick test
In a seperate terminal:
```bash 
curl http://localhost:8000/health
```
