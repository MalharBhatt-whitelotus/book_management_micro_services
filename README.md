# Book Management Microservices

## Overview

Book Management Microservices is a modular FastAPI application built
using a microservice architecture. The project consists of an API
Gateway that routes requests to independent services responsible for
users, books, bills, and AI-powered knowledge retrieval.

### Microservices

```
  -----------------------------------------------------------------------
  Service              Port          Responsibility
  -------------------- ------------- ------------------------------------
  API Gateway          8000          Entry point, HTML pages, request
                                     routing

  User Service         8001          Authentication, JWT, user management

  Book Service         8002          Book CRUD, uploads, search,
                                     pagination

  Bill Service         8003          Checkout and billing

  AI Knowledge Service 8004          PDF ingestion and AI question
                                     answering
  -----------------------------------------------------------------------
```

## Features

-   FastAPI Microservices
-   API Gateway
-   Automatic service startup
-   Automatic service monitoring
-   Automatic restart of failed services
-   Automatic shutdown of child services
-   JWT Authentication
-   PostgreSQL databases
-   SQLAlchemy ORM
-   Alembic migrations
-   Async database access
-   Repository-Service architecture
-   Jinja2 frontend
-   File upload support
-   AI knowledge base integration
-   Pytest support

## Architecture

``` text
Browser
   |
API Gateway (8000)
   |
   +--> User Service (8001)
   +--> Book Service (8002)
   +--> Bill Service (8003)
   +--> AI Knowledge Service (8004)

Service Manager
- Starts services
- Monitors services
- Restarts crashed services
- Stops services on shutdown
```

## Technologies

-   Python
-   FastAPI
-   SQLAlchemy
-   PostgreSQL
-   AsyncPG
-   Alembic
-   Pydantic
-   JWT
-   Passlib
-   Jinja2
-   HTML/CSS/JavaScript
-   Pytest

## Running

``` bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn book_management_application.app.main:app
```

Starting the API Gateway automatically launches the User, Book, Bill,
and AI Knowledge services.

## Databases

Each service owns its own PostgreSQL database.

-   user
-   book
-   bill
-   knowledge

## Service Manager

The custom Service Manager:

-   Launches child services
-   Continuously monitors them
-   Restarts crashed services
-   Keeps the gateway alive
-   Gracefully shuts down all services

## Authentication

-   JWT Access Tokens
-   Password hashing using bcrypt
-   Protected endpoints

## Testing

``` bash
pytest
```

## Future Improvements

-   Docker
-   Docker Compose
-   Redis
-   RabbitMQ
-   Kubernetes
-   Prometheus
-   Grafana
-   CI/CD

## Author

**Malhar Bhatt**
