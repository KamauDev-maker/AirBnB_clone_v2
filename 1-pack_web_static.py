#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static
"""


from fabric.api import local
from datetime import datetime

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
