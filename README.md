# Inschooltech - Lab System API

## Features

- Entity creation with django admin site (labs, tests, indicators, metrics, scores, etc.);

- Test filtration against lab_id;

- LocMem django sub-system used;

- Token authorization;

- Swagger documentation;

- PostgreSQL DB used;

- Docker compose for developing and production deployment;

- CI/CD (GitHub based, linters (flake8, mypy), tests);

- Pytest for testing.

## How to run server locally

- Clone repo

```git clone git@github.com:AlexanderUp/labs_inschooltech.git```

- Create virtual environment

```python3 -m venv venv```

- Activate virtual environment

```source venv/bin/activate```

- Install dependencies (no development dependencies like flake8, etc.)

```python3 -m pip install -r requirements/base.txt```

- Install dependencies (with development dependencies like flake8, etc.)

```python3 -m pip install -r requirements/dev.txt```

- Install dependencies (with test dependencies like pytest, etc.)

```python3 -m pip install -r requirements/test.txt```

- Create .env file in lab_project (where .env.example is) and set django secret key
(path to file - ./lab_project/lab_project)

### Run server in development mode

- Change dir to infra/dev, create and populate file .env like infra/example.env

!!! POSTGRES_HOST=localhost

- Start Postgres container:

```docker-compose up```

- Apply migrations

```python3 manage.py migrate```

- Create superuser

```python3 manage.py createsuperuser```

- Run server

```python3 manage.py runserver```

- Server is running at ```http://127.0.0.1:8000```

- API description is available with Swagger or Redoc at

```http://127.0.0.1:8000/swagger/```

```http://127.0.0.1:8000/redoc/```

- Run tests (change dir to root dir)

```cd ../..```

```python3 -m pytest ..```

- Stop and remove container:

```docker-compose down```

- Stop and remove container and data volume:

```docker-compose down -v```


### Run server in development mode

- Change dir to infra/prod, create and populate file .env like infra/example.env

!!! POSTGRES_HOST=postgres

- Start compose services:

```docker-compose up```

- Create superuser

```docker-compose exec web python3 manage.py createsuperuser```

- Server is running at ```http://127.0.0.1```

- API description is available with Swagger or Redoc at

```http://127.0.0.1/swagger/```

```http://127.0.0.1/redoc/```

- Stop and remove container:

```docker-compose down```

- Stop and remove container and data volume:

```docker-compose down -v```


### Authentication

Token based authentication used.

Example:

Header 'AUTORIZATION': 'Token Token 9e96a48287b05c4270386ebd69216a246b3d27f9'.

Token obtaining available at

```http://127.0.0.1/api-token-auth/``` (production)

```http://127.0.0.1:8000/api-token-auth/``` (development)

with POST

```json
{
    "username": "john_doe",
    "password": "super_secret_password"
}
```
