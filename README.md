# Booking System — Room & Resource Scheduling

A comprehensive, production-ready booking and scheduling platform: admin-managed resources, weekly availability rules, blackout dates, buffer-time enforcement, race-condition-safe double-booking prevention, recurring bookings, cancellation policy, notifications, and interactive calendar UI.

## Dependencies

- **Python:** 3.10+
- **Framework:** Django 5.x, Django REST Framework
- **Authentication:** `djangorestframework-simplejwt`
- **Database:** PostgreSQL (production) / SQLite (development/testing)
- **Containerization:** Docker & Docker Compose
- **Testing:** pytest, pytest-django

All dependencies are defined in `requirements.txt`, `pyproject.toml`, and `poetry.lock`.

## Installation

### 1. Set up Virtual Environment & Install Dependencies

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

### 2. Environment Configuration

```bash
cp env.example .env
# Configure SECRET_KEY and DB settings in .env
```

## Build

### Option A: Local Build & Migration

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
```

### Option B: Docker Build

```bash
docker build -t booking-system .
```

Or using Makefile:
```bash
make install
make migrate
make docker-build
```

## Run

### Option A: Direct Python Entry Point

```bash
python main.py
# or
python app.py
# or
python manage.py runserver 0.0.0.0:8000
```

### Option B: Docker Run

```bash
docker run -p 8000:8000 booking-system
```

Or using docker-compose:
```bash
docker-compose up
```

Access the application:
- **Web UI & Calendar:** http://127.0.0.1:8000/
- **Admin Portal:** http://127.0.0.1:8000/admin/
- **Swagger / OpenAPI Documentation:** http://127.0.0.1:8000/api/docs/

## Usage

### 1. Seed Demo Data
```bash
python manage.py seed_demo
```

### 2. Run Test Suite
```bash
pytest
# or
make test
```

### 3. API Endpoints
- `POST /api/token/` - Obtain JWT Token
- `POST /api/accounts/register/` - Register User
- `GET /api/accounts/me/` - Current User Profile
- `GET /api/resources/resources/` - List Available Resources
- `GET /api/bookings/calendar/` - FullCalendar Feed
- `POST /api/bookings/` - Create New Booking
- `POST /api/bookings/{id}/cancel/` - Cancel Booking

## License

Proprietary. All rights reserved. (No open source license).
