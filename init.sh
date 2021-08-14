sudo /etc/init.d/nginx restart
cd ask/
gunicorn --bind='0.0.0.0:8000' ask.wsgi:application
