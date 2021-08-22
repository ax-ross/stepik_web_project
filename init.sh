sudo /etc/init.d/nginx restart
cd ask/
sudo /etc/init.d/mysql start
sudo mysql -uroot -e "CREATE DATABASE db"
sudo python3 /home/box/web/ask/manage.py makemigrations
sudo python3 /home/box/web/ask/manage.py migrate
gunicorn --bind='0.0.0.0:8000' ask.wsgi:application
