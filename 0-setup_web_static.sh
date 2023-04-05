#!/usr/bin/env bash
# That sets up your web servers for the deployment of web_static
sudo apt-get update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/static/releases/test/
echo "<html>
<head>
</head>
<body>
Holberton School
</body>
</html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '/server_name _;/a \ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart
