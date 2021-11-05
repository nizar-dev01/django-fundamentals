#!/bin/bash
cp /home/ubuntu/baby-django/server.conf /etc/nginx/sites-available
ln -s /etc/nginx/sites-available/server.conf /etc/nginx/sites-enabled
sed -i 's/# server_names_hash_bucket_size 64;/server_names_hash_bucket_size 128;/g' /etc/nginx/nginx.conf
