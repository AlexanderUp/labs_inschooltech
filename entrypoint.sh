#!/bin/sh

python3 manage.py migrate --noinput

python3 manage.py collectstatic --noinput

gunicorn lab_project.wsgi:application --bind 0:8000
