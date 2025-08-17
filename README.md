# 3-Tier-Modular-Monolith

## Overview

This project implements a 3-tier modular monolith backend application using **FastAPI**. The system is designed to be modular, maintainable, and easily extensible. The project supports **user management** and a **health check endpoint**, backed by a **PostgreSQL database** running in Docker.

**Completed so far (Tasks 1–17):**

* Project setup with virtual environment
* FastAPI application setup with lifespan context
* PostgreSQL database connection using `asyncpg` connection pool
* User model and CRUD service
* User API endpoints (`create_user`, `get_user`, `list_users`)
* Health check API
* Table creation in PostgreSQL on startup
* Testing setup (can test APIs via FastAPI docs)

---

## File Structure

```
.
├── .gitignore
├── LICENSE
├── README.md
├── backend
│   ├── __init__.py
│   ├── api
│   │   └── routes
│   │       ├── __init__.py
│   │       ├── health_routes.py
│   │       ├── test_db.py
│   │       └── user_routes.py
│   ├── database
│   │   ├── __init__.py
│   │   └── db_config.py
│   ├── db
│   │   ├── __init__.py
│   │   └── database.py
│   ├── main.py
│   ├── models
│   │   ├── __init__.py
│   │   └── user.py
│   └── services
│       ├── __init__.py
│       └── user_service.py
├── backend/tests
│   └── __init__.py
├── folder_snapshot.txt
├── requirements.txt
└── run.py
```

---

## Tools & Technologies

| Tool/Technology | Version / Notes   |
| --------------- | ----------------- |
| Python          | 3.12              |
| FastAPI         | Latest            |
| asyncpg         | Latest            |
| PostgreSQL      | 16.x (via Docker) |
| Docker          | Latest            |
| Uvicorn         | Latest            |
| Pydantic        | Latest            |

---

## Setting Up PostgreSQL in Docker

1. Pull and run PostgreSQL Docker container:

```bash
docker run -d \
  --name modular-monolith-postgres \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=testdb \
  -p 5432:5432 \
  postgres:16
```

2. Ensure container is running:

```bash
docker ps
```

---

## Running the Application

1. Create and activate virtual environment:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python run.py
```

4. Visit FastAPI docs to test endpoints:

```
http://127.0.0.1:8082/docs
```

**Available endpoints:**

* `/api/health` – Health check
* `/users/users` – Create a user (POST)
* `/users/users/{user_id}` – Get user by ID (GET)
* `/users/users` – List all users (GET)

---

## Notes

* The application automatically creates the `users` table on startup if it does not exist.
* Testing endpoints can be done directly from the FastAPI interactive docs.
* All database operations are asynchronous using `asyncpg`.

## Next Steps / Timeline
### Dockerize the Application

- Containerize backend API using Docker
- Include PostgreSQL in Docker Compose (optional)
- Ensure environment variables are properly injected
- Verify endpoints work inside containers

### Epic 2: Deploy to AWS

- Prepare Terraform scripts for infrastructure
- Deploy API to AWS ECS / Fargate
- Setup RDS for PostgreSQL in AWS
- Configure Load Balancer and networking

### Epic 3: CI/CD with GitHub Actions

- Setup GitHub Actions workflow
- Run automated tests on push / pull request
- Automate Docker build and push to ECR
- Deploy API updates automatically to AWS
