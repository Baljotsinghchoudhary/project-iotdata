release: python manage.py migrate --noinput
web: gunicorn cloudAgri.wsgi --log-file -
worker: python manage.py process_tasks 