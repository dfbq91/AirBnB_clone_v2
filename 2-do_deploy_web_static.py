#!/usr/bin/python3
from datetime import datetime
from fabric.api import put, run, env
import os.path


def do_deploy(archive_path):
    '''distributes an archive to your web servers'''

    env.hosts = ['34.74.97.226', '18.209.18.155']
    env.user = "ubuntu"

    if os.path.exists(archive_path) is False:
        return False

    file_non_ver = archive_path.replace("versions/", "")
    file_non_ext = file_non_ver.replace(".tgz", "")
    p1 = "/data/web_static/releases/"

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")

        # Create path where to uncompress file_without_versions
        run("mkdir -p /data/web_static/releases/{}/".
            format(file_non_ext))

        # Uncompress the archive to a folder
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
            format(file_non_ver, file_non_ext))

        # Delete the archive from the web server
        run("rm /tmp/{}".format(file_non_ver))

        # Move web static files one directory level up
        run("mv {}{}/web_static/* {}{}/".
            format(p1, file_non_ext, p1, file_non_ext))

        # Delete old path of the recently moved files
        run("rm -rf /data/web_static/releases/{}/web_static".
            format(file_non_ext))

        # Delete the symbolic link /data/web_static/current from the web server
        run("rm -rf /data/web_static/current")

        # New sym link
        run("ln -s /data/web_static/releases/{} /data/web_static/current".
            format(file_non_ext))

        return True

    except:
        print("hubo error")
        return False
