NGINX_SITES="/etc/nginx/sites-enabled"
SERVER_ROOT="/home/box/web"
NGINX_EXEC="/etc/init.d/nginx"
GUNICORN_SITES="/etc/gunicorn.d"
GUNICORN_EXEC="/etc/init.d/gunicorn"

sudo test -h ${NGINX_SITES}/default && sudo rm ${NGINX_SITES}/default
sudo ln -sf ${SERVER_ROOT}/etc/nginx.conf ${NGINX_SITES}/stepic.conf
sudo ${NGINX_EXEC} restart
sudo ln -sf ${SERVER_ROOT}/etc/gunicorn_test.conf   ${GUNICORN_SITES}/test
sudo ln -sf ${SERVER_ROOT}/etc/gunicorn_ask.conf ${GUNICORN_SITES}/ask
#sudo mysql -uroot -e "source create_db.sql"
#sudo python ask/manage.py makemigrations
#sudo python ask/manage.py migrate
sudo python ask/manage.py syncdb
sudo ${GUNICORN_EXEC} restart
sudo chown www-data:www-data ask/
sudo chown www-data:www-data ask/db.sqlite3

