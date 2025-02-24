# Shared Ledger System

## Overview

This project is a Shared Ledger System designed for a monorepo containing multiple applications. It provides a centralized ledger system to track user credits across different applications while ensuring code reuse, type safety, and extensibility.

The system is built using modern Python technologies, including FastAPI, SQLAlchemy, Pydantic, and Alembic, and is designed to be scalable and maintainable.

## Features
**Shared Ledger Operations:** Core ledger functionality is shared across applications, with support for app-specific operations.

**Type Safety:** Enforced through Python's Enum and Pydantic models.

**Extensibility:** Applications can extend the base ledger operations with their own custom operations.

**Database Isolation:** Each application uses its own schema within the same database, ensuring data isolation.

**RESTful API:** Provides endpoints to manage ledger entries and query balances.

## Technical Requirements
The project is implemented using the following technologies:

**Python** ≥ 3.10

**FastAPI** (for building the API)

**SQLAlchemy** ≥ 2.0.0 (for database interactions)

**Pydantic** (for data validation and serialization)

**Alembic** (for database migrations)

**PostgreSQL** (as the database)

## Getting Started

### Prerequisites
Before running the project, ensure you have the following installed:

Python 3.10 or higher

PostgreSQL (or a compatible database)

### Installation

1. Clone the repository
```bash
git clone https://github.com/your-username/shared-ledger-system.git
cd shared-ledger-system
```

2. Create a virtual environment
```bash
python -m venv venv
```

3. Activate virtual environment:

- For Unix based (Linux & macOS) systems:
```bash
source venv/bin/activate
```

- For Windows based systems:
```bash
.\venv\Scripts\activate
```

4. Install the required Python packages using pip:
```bash
pip install -r requirements.txt
```

5. Configure the database:

- Create a PostgreSQL database.
- Update the database connection strings in **.env** file:
```python
POSTGRES_DB=sharedledgerdb
POSTGRES_USER=dbuser
POSTGRES_PASSWORD=1234
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

6. Run migrations:
- For healthai app:
```bash
cd monorepo\healthai
alembic upgrade head
```

- For travelai app:
```bash
cd monorepo\travelai
alembic upgrade head
```

7. Start the application:
```bash
cd ..
cd ..
uvicorn monorepo.main: app --reload
```

### Testing
To run the tests, use the following command:
```bash
pytest monorepo/tests/
```

### Additional Information
For more detailed information on FastAPI, Alembic, SqlAlchemy and Pydantic; consult their respective documentation:

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/en/latest/tutorial.html)
- [SqlAlchemy Documentation](https://docs.sqlalchemy.org/en/20/)
- [Pydantic Documentation](https://docs.pydantic.dev/latest/)
