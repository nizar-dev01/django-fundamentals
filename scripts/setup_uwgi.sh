#!/bin/bash
uwsgi --ini /home/ubuntu/baby-django/app_uwsgi.ini
mkdir /home/ubuntu/app/vassals
cp /home/ubuntu/baby-django/emperor.uwsgi.service /etc/systemd/system
systemctl enable emperor.uwsgi.service
systemctl start emperor.uwsgi.service
service nginx restart