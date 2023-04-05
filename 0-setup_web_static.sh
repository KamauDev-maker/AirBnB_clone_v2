#!/usr/bin/env bash
# That sets up your web servers for the deployment of web_static
sudo apt-get update
sudo apt-get -y install nginx
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/static/releases/test/
echo '<html>
<head>
</head>
<body>
Best School
</body>
</html>' | sudo tee /data/web_static/releases/test/index.html
ln -s /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data
sed -i "/listen 80 default_server;/a location /hbnb_static {alias /data/web_static/current/;}" /etc/nginx/sites-available/default
service nginx restart
