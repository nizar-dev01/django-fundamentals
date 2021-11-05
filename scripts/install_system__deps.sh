#!/bin/bash
apt-get update
apt-get install build-essential git python3 python3-pip python3-venv nginx -y
pip3 install uwsgi
systemctl start nginx.service