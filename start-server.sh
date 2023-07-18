#!/usr/bin/env bash
# start-server.sh
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    ( cd sig-despensa/; python manage.py createsuperuser --no-input; python manage.py migrate; python manage.py loaddata sample)
fi
(cd sig-despensa/; gunicorn app.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3) &
nginx -g "daemon off;"