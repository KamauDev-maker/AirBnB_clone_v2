#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers,
"""

import os
from fabric.api import run, put, env
from os.path import exists


env.hosts = ['3.84.238.176', '52.87.233.7']


def do_deploy(archive_path):
    """
    a method that distributes an archive to your web servers and deploy it
    """
    if not os.path.exists(archive_path):
        return False
    filename = os.path.basename(archive_path)
    filename_without_ext = filename.replace(".tgz", "")
    filepath = "/data/web_static/releases/{}/".format(filename_without_ext)
    success = False
    try:
        # upload the archive to the /tmp/
        put(archive_path, '/tmp/{}'.format(filename))

        # Uncompress the archive to /data/web_static/releases/<archive
        run("mkdir -p {}".format(filepath))
        run("tar -xzf /tmp/{} -C {}".format(filename, filepath))

        # Delete the archive from the web server
        run("rm -rf /tmp/{}".format(filename))
        run("mv {}web_static/* {}".format(filepath, filepath))
        run("rm -rf {}web_static".format(filepath))

        # Delete the symbolic link
        run("sudo rm -f /data/web_static/current")

        # Create a new the symbolic link
        run("sudo ln -s {} /data/web_static/current".format(filepath))
        print("New version deployed!")
        success = True
    except BaseException:
        success = False
    return success
