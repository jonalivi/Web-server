sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/stepic.conf
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
#sudo /etc/init.d/gunicorn restart
sudo /usr/bin/gunicorn -D 0.0.0.0:8080 hello:app
