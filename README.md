# Habit Tracker API

A backend REST API for tracking daily habits and calculating completion streaks.

This project was built to practice backend engineering concepts such as relational database modeling, service-layer architecture, and database migrations.

---

## Tech Stack

- **Python 3.12**
- **FastAPI**
- **PostgreSQL**
- **SQLAlchemy (ORM)**
- **Alembic (database migrations)**
- **Pydantic**

---

## Features

- Create, update, and delete habits
- Record daily habit completions
- Prevent duplicate completions per day
- Track completion history
- Calculate statistics:
  - Total completions
  - Current streak
  - Longest streak

- Database schema versioning with Alembic

---

## Project Structure

```
habit_tracker/
│
├── app/
│   ├── main.py
│   │
│   ├── database/
│   │   ├── base.py
│   │   ├── models.py
│   │   └── session.py
│   │
│   ├── routers/
│   │   ├── habit.py
│   │   └── completion.py
│   │
│   ├── schemas/
│   │   ├── habit.py
│   │   └── completion.py
│   │
│   └── services/
│   │   ├── habit_service.py
│   │   └── completion_service.py
│
├── migrations/
│
├── alembic.ini
├── requirements.txt
└── .env
```

---

## Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/suleymangulymalikov/habit_tracker.git
```

```
cd habit_tracker
```

### 2. Create virtual environment

```
python -m venv .venv
```

Activate:

**Windows**

```
.venv\Scripts\activate
```

**Mac/Linux**

```
source .venv/bin/activate
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

### 4. Configure environment variables

Create a `.env` file in the project root.

Example:

```
DATABASE_URL=postgresql+psycopg://postgres:password@localhost:5432/habit_tracker
```

---

## Database Setup

Run migrations to create the database schema:

```
alembic upgrade head
```

---

## Running the API

Start the server:

```
fastapi dev .\app\main.py
```

API will be available at:

```
http://127.0.0.1:8000
```

Interactive documentation:

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Habits

```
POST   /habits
GET    /habits
GET    /habits/{id}
PUT    /habits/{id}
DELETE /habits/{id}
```

### Habit Completions

```
GET    /habits/{habit_id}/completions
POST   /habits/{habit_id}/complete
GET    /habits/{habit_id}/stats
```

---

## Database Migrations

Generate migration after modifying models:

```
alembic revision --autogenerate -m "description"
```

Apply migrations:

```
alembic upgrade head
```

graph TD
Client --> FastAPI
FastAPI --> HabitRouter
FastAPI --> CompletionRouter
HabitRouter --> HabitService
CompletionRouter --> CompletionService
HabitService --> PostgreSQL
CompletionService --> PostgreSQL
