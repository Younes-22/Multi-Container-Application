# 🐳 Flask + Redis Multi-Container App

This project is a multi-container web application built with **Flask** and **Redis**, managed via **Docker Compose**. The app displays a welcome message and keeps track of visit counts using Redis as a key-value store.

---

## 📦 Features

- Python Flask web server
- Redis for storing visit count
- Multi-container setup using Docker Compose
- Persistent Redis data via Docker volumes
- Environment-based configuration via `docker-compose.yml`

---

## 🚀 Getting Started

### ✅ Prerequisites

- Docker
- Docker Compose

### 🧰 Run the Application

```bash
docker compose up --build

Access the app at: http://localhost:5001

Visit the /count endpoint to increment and display the visit count

### Scaling 
docker-compose up --scale flask=3
Change ports to expose as 3 instances can't run on one port

the expose directive makes the flask app port 5001 available to other services in the docker network but dosen't bind it to the host network

whilst the application can scale internally, it's not directly accessible from the host because we removed the host port binding

now we need to use a load balancer and reverse proxy that can distribute incoming traffic to the multiple instances of my flask app

the reason we use a reverse proxy is because we have multiple instances and we can't bind to a port on each instance. so instead we bind to a port on a reverse proxy then becomes a single point of accessing our application. the reverse proxt ill use is nginx

need to understand what nginx service in docker-compose and nignx.conf do