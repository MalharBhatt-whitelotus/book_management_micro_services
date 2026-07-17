# Book Management System - Microservices Architecture

A modern **Book Management System** built using **FastAPI Microservices Architecture**. The application follows a modular and scalable design where each business domain is implemented as an independent microservice and managed through a centralized **API Gateway**.

The API Gateway automatically starts, monitors, and stops all microservices, providing a single entry point for the application.

---

# Features

## API Gateway

* Central entry point for all client requests
* Automatically starts all backend microservices
* Automatically stops all microservices when the gateway shuts down
* Monitors running services in the background
* Automatically restarts any crashed service
* Continues running even if one or more child services terminate
* Jinja2-based HTML frontend
* Reverse proxy endpoints for all backend services

---

## User Service

* User Registration
* User Login
* JWT Authentication
* Password Hashing
* User Profile Management

---

## Book Service

* Add Book
* Update Book
* Delete Book
* Search Books
* Upload Book Cover Image
* Upload Book PDF
* Pagination
* Book Statistics
* Inventory Management

---

## Bill Service

* Checkout Books
* Bill Generation
* Purchase History
* Stock Management
* Order Summary

---

# Service Manager

The API Gateway includes a custom **Service Manager** responsible for managing all microservices.

## Responsibilities

* Starts all services automatically during gateway startup.
* Stops every service during gateway shutdown.
* Continuously monitors all running services.
* Automatically restarts any crashed service.
* Keeps the API Gateway running even if a child service terminates unexpectedly.

---

# Architecture

```text
                           +----------------------+
                           |     API Gateway      |
                           |       Port 8000      |
                           +----------+-----------+
                                      |
        --------------------------------------------------------
        |                     |                     |
        ▼                     ▼                     ▼
+---------------+     +---------------+     +---------------+
| User Service  |     | Book Service  |     | Bill Service  |
|    8001       |     |    8002       |     |    8003       |
+---------------+     +---------------+     +---------------+

           ▲
           |
     Service Manager
           |
    --------------------
    | Start Services   |
    | Monitor Services |
    | Restart Services |
    | Stop Services    |
    --------------------
```

---

# Tech Stack

## Backend

* Python
* FastAPI
* SQLAlchemy
* Pydantic
* PostgreSQL
* Async SQLAlchemy
* Uvicorn

## Frontend

* HTML
* CSS
* Vanilla JavaScript
* Jinja2 Templates

## Authentication

* JWT
* OAuth2 Password Flow
* Passlib (bcrypt)

---

# Project Structure

```text
book_management_application/
│
├── app/
│   ├── main.py
│   ├── service_manager.py
│   │
│   ├── routers/
│   │   ├── view_router.py
│   │   ├── user_service_routes.py
│   │   ├── book_service_routes.py
│   │   └── bill_service_routes.py
│   │
│   ├── templates/
│   └── static/
│
├── user_services/
│   └── app/
│       ├── main.py
│       ├── user_routes.py
│       ├── user_services.py
│       ├── user_repository.py
│       ├── user_models.py
│       ├── user_schema.py
│       ├── user_database.py
│       └── security.py
│
├── book_services/
│   └── app/
│       ├── main.py
│       ├── book_routes.py
│       ├── book_services.py
│       ├── book_repository.py
│       ├── book_models.py
│       ├── book_schema.py
│       ├── book_database.py
│       └── uploads/
│
├── bill_services/
│   └── app/
│       ├── main.py
│       ├── bill_routes.py
│       ├── bill_services.py
│       ├── bill_repository.py
│       ├── bill_models.py
│       ├── bill_schema.py
│       └── bill_database.py
│
├── requirements.txt
├── README.md
└── .env
```

---

# Microservices

## API Gateway (Port 8000)

Responsibilities

* Serves HTML pages
* Routes frontend requests
* Proxies API requests
* Starts all backend services
* Monitors services
* Restarts failed services

---

## User Service (Port 8001)

Features

* User Registration
* Login
* JWT Token Generation
* User Authentication
* Password Encryption

---

## Book Service (Port 8002)

Features

* Add Book
* Update Book
* Delete Book
* Search Book
* Pagination
* Upload Cover Image
* Upload PDF Document
* Inventory Statistics

---

## Bill Service (Port 8003)

Features

* Checkout Books
* Create Bills
* Bill History
* Purchase Details
* Quantity Validation

---

# Databases

Each microservice owns its own PostgreSQL database.

| Service      | Database |
| ------------ | -------- |
| User Service | user     |
| Book Service | book     |
| Bill Service | bill     |

This follows the **Database per Service** pattern commonly used in Microservice Architecture.

---

# API Gateway Routes

The Gateway exposes routes that internally communicate with the appropriate microservice.

Examples:

```http
GET    /
POST   /login
POST   /register

GET    /books
POST   /books
PUT    /books/{id}
DELETE /books/{id}

POST   /checkout
GET    /bill/{id}
```

The client communicates only with the API Gateway.

---

# Service Lifecycle

## Startup

When the API Gateway starts:

1. User Service starts.
2. Book Service starts.
3. Bill Service starts.
4. Monitor thread starts.
5. Gateway becomes available.

---

## Runtime

The Service Manager continuously checks whether each service is alive.

If a service crashes:

* Detects the failure.
* Starts a new instance.
* Updates the internal process reference.
* Gateway continues serving requests.

---

## Shutdown

When the API Gateway stops:

1. Monitor thread exits.
2. User Service stops.
3. Book Service stops.
4. Bill Service stops.
5. Gateway exits cleanly.

---

# Frontend Dashboard

The application includes a responsive dashboard built with:

* HTML
* CSS
* Vanilla JavaScript
* Jinja2

Features include:

* Login Page
* Registration Page
* Dashboard
* Book Inventory
* Pagination
* Search
* Statistics Cards
* Dark / Light Theme
* Toast Notifications
* Responsive Layout

---

# Security

* JWT Authentication
* OAuth2 Password Bearer
* Password Hashing using bcrypt
* Protected API Endpoints

---

# Running the Project

## 1. Clone the Repository

```bash
git clone <repository-url>
cd book_management_application
```

---

## 2. Create Virtual Environment

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file with your PostgreSQL credentials and application settings.

Example:

```env
USER_DB_URL=postgresql+asyncpg://username:password@localhost:5432/user
BOOK_DB_URL=postgresql+asyncpg://username:password@localhost:5432/book
BILL_DB_URL=postgresql+asyncpg://username:password@localhost:5432/bill

SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## 5. Start the Application

Only the API Gateway needs to be started.

```bash
uvicorn book_management_application.app.main:app
```

The gateway automatically starts:

* User Service (8001)
* Book Service (8002)
* Bill Service (8003)

---

# Future Improvements

* Docker Support
* Docker Compose
* Redis Caching
* RabbitMQ / Kafka
* Service Discovery
* Health Check Endpoints
* API Rate Limiting
* Circuit Breaker Pattern
* Distributed Logging
* Prometheus Monitoring
* Grafana Dashboard
* Kubernetes Deployment
* CI/CD Pipeline

---

# Author

**Malhar Bhatt**

---

# License

This project is intended for educational, learning, and portfolio purposes.

You may modify and use this project for personal or academic work.
