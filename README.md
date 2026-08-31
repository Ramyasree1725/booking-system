# Booking System — Room/Resource Scheduling (Django + DRF + PostgreSQL)

A full booking platform: admin-managed resources, weekly availability rules, blackout dates, buffer-time enforcement, race-condition-safe double-booking prevention (Postgres exclusion constraint), recurring bookings, cancellation policy, email notifications, and a FullCalendar-based UI.

## Stack

- **Backend:** Django 5 + Django REST Framework
- **Database:** PostgreSQL (uses `tstzrange` + an `ExclusionConstraint` — this is not optional for production race-safety; SQLite works for local demo via `USE_SQLITE=True`)
- **Auth:** JWT (`djangorestframework-simplejwt`), roles via a `role` field on the custom `User` model
- **Frontend:** Django templates + FullCalendar.js (CDN), calling the DRF API
- **Notifications:** Django email backend (console by default; swap in SMTP for production)
- **API Docs:** OpenAPI via drf-spectacular at `/api/docs/`

## Features

- Resource categories and bookable resources (rooms, equipment, etc.)
- Weekly availability rules per resource
- Blackout dates (global or per-resource)
- Configurable buffer time between bookings
- Min/max duration enforcement
- Advance booking window
- Optional approval workflow
- Conflict detection with buffer
- JWT + session auth
- FullCalendar interactive UI
- Email notifications on create / cancel / approve
- Role-based access (admin / staff / user)

## Setup

### 1. Clone & virtualenv

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Environment

```bash
cp .env.example .env
# Edit .env — set SECRET_KEY, DB_* for PostgreSQL
```

For a quick local demo without Postgres:

```bash
export USE_SQLITE=True
```

### 3. Database

**PostgreSQL (recommended):**

```bash
createdb booking_system
python manage.py makemigrations
python manage.py migrate
```

**SQLite (demo only):**

```bash
export USE_SQLITE=True
python manage.py makemigrations
python manage.py migrate
```

### 4. Superuser & run

```bash
python manage.py createsuperuser
python manage.py runserver
```

Visit:

- **App / Calendar:** http://127.0.0.1:8000/
- **Admin:** http://127.0.0.1:8000/admin/
- **API Docs (Swagger):** http://127.0.0.1:8000/api/docs/
- **API Schema:** http://127.0.0.1:8000/api/schema/

### 5. Tests

```bash
pytest --cov=accounts --cov=resources --cov=bookings --cov-report=term-missing
```

## API Overview

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/token/` | Obtain JWT |
| POST | `/api/accounts/register/` | Register user |
| GET | `/api/accounts/me/` | Current user |
| GET/POST | `/api/resources/resources/` | List / create resources |
| GET | `/api/resources/resources/{slug}/availability/` | Rules + blackouts |
| GET/POST | `/api/bookings/` | List / create bookings |
| POST | `/api/bookings/{id}/cancel/` | Cancel booking |
| GET | `/api/bookings/calendar/` | FullCalendar feed |
| GET | `/api/bookings/available_slots/?resource=&date=` | Free slots |

## Project structure

```
booking_system/
├── accounts/          # Custom User, auth, profile
├── resources/         # Categories, resources, availability, blackouts
├── bookings/          # Booking model, services, conflict logic, API
├── booking/           # Project settings, urls, wsgi
├── frontend/static/   # CSS + calendar JS
├── templates/         # Django templates (calendar, login)
├── tests/             # pytest suite
├── manage.py
├── requirements.txt
├── .env.example
└── README.md
```

## Production notes

1. Set `DEBUG=False`, strong `SECRET_KEY`, and proper `ALLOWED_HOSTS`.
2. Use PostgreSQL and enable the exclusion constraint migration for race-safe bookings.
3. Configure real SMTP for email.
4. Serve with gunicorn + nginx (or similar) and collectstatic.
5. Put Redis/Celery in front if you add async reminders.

## License

Proprietary — all rights reserved. Not open source.
