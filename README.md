# podman-api

A simple Flask API containerized with Podman

## Prerequisites
- Tested on macOS with Podman version 5.8.0 and Podman-Compose version 1.5.0 installed via HomeBrew


## Build & Run
```bash
podman compose up --build
```

## Test API health
In a seperate terminal:
```bash 
curl http://localhost:8000/health
```

## Test DB health
In a seperate terminal:
```bash
curl http://localhost:8000/db-health
```
