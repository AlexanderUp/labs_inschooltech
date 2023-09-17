FROM python:3.11.5-slim

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install gettext libpq-dev gcc -y

RUN mkdir /app

COPY requirements/ /app/requirements

RUN pip install --upgrade pip

RUN pip3 install -r /app/requirements/prod.txt --no-cache-dir

COPY lab_project/ /app/lab_project

WORKDIR /app/lab_project

CMD ["python3", "manage.py", "runserver", "0:8000"]
