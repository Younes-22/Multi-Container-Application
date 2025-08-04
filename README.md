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