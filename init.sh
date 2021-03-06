#!/bin/bash

sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default

sudo /etc/init.d/nginx restart

sudo ln -sf /home/box/web/etc/gunicorn.conf.py   /etc/gunicorn.d/test
sudo ln -sf /home/box/web/etc/gunicorn_django.conf.py   /etc/gunicorn.d/django

sudo /etc/init.d/gunicorn restart
