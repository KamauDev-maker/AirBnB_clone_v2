#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers,
"""


from fabric.api import run, put, env
from os.path import exists


env.hosts = ['3.84.238.176', '52.87.233.7']


def do_deploy(archive_path):
    """
    a method that distributes an archive to your web servers and deploy it
    """
    if not exists(archive_path):
        return False
    try:
        # upload the archive to the /tmp/
        put(archive_path, '/tmp/')

        # filename without extension
        filename = archive_path.split('/')[-1]
        filename_without_ext = filename.split('.')[0]

        # Uncompress the archive to /data/web_static/releases/<archive
        run("mkdir -p /data/web_static/releases/{}"
            .format(filename_without_ext))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(filename, filename_without_ext))

        # Delete the archive from the web server
        run("rm /tmp/{}".format(filename))

        # Delete the symbolic link
        run("sudo rm -f /data/web_static/current")

        # Create a new the symbolic link
        run("sudo ln -s /data/web_static/releases/{}/ "
            "/data/web_static/current".format(filename_without_ext))

        return True
    except BaseException:
        return False
