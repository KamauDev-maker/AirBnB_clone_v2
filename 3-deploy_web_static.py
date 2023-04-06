#!/usr/bin/python3
"""
that creates and distributes an archive to your web servers
"""


import os
from datetime import datetime
from fabric.api import env, put, local, run


env.hosts = ['3.84.238.176', '52.87.233.7']


def do_pack():
    """
    generates a .tgz archive from the contents of the web_static
    with a time-stamp
    """
    now = datetime.now()
    time = now.strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(time)

    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/{} web_static".format(archive_name))
        return "versions/{}".format(archive_name)
    except BaseException:
        return None


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


def deploy():
    """
    distributes an archive to your web servers
    """
    updated_archive_path = do_pack()
    if exists(updated_archive_path) is False:
        return False
    result = do_deploy(updated_archive_path)
    return result
