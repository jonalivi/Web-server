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
sudo ${GUNICORN_EXEC} restart

