#!/bin/bash
cd app

echo Running migrations
python manage.py migrate --noinput

echo Collectin staticfiles
python manage.py collectstatic --no-input --clear

echo Running server with gunicorn
gunicorn core.wsgi:application --workers 3 --bind 0.0.0.0:80
