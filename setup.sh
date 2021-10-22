#!/bin/bash
sudo apt update -y
sudo apt-get update && \
sudo apt-get install \
    build-essential \
    git \
    python3 \
    python3-pip \
    python3-venv \
    nginx -y \
&& pip3 install uwsgi
python3 -m venv ~/app;
source ~/app/bin/activate
pip3 install django
git clone https://github.com/nizar-dev01/baby-django.git
sudo cp ~/baby-django/server.conf /etc/nginx/sites-available
sudo ln -s /etc/nginx/sites-available/server.conf /etc/nginx/sites-enabled

sudo sed -i 's/# server_names_hash_bucket_size 64;/server_names_hash_bucket_size 128;/g' /etc/nginx/nginx.conf
sudo service nginx restart
# Test server
# uwsgi --socket ~/baby-django/app.sock --module app.wsgi --chmod-socket=666
# Init the actual server
uwsgi --ini ~/baby-django/app_uwsgi.ini

# Complete the configuration
mkdir ~/app/vassals
uwsgi --emperor ~/app/vassals --uid www-data --gid www-data

