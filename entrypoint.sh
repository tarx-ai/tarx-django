#!/bin/bash
cd app
sleep 5
echo Running migrations
python manage.py migrate --noinput

echo Collectin staticfiles
python manage.py collectstatic --no-input --clear

echo Running server with gunicorn
gunicorn core.wsgi:application --bind 0.0.0.0:80
