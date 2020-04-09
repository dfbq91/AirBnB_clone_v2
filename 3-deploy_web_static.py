#!/usr/bin/python3
from datetime import datetime
from fabric.api import local, put, run, env
import os.path

env.hosts = ['34.74.97.226', '18.209.18.155']
env.user = "ubuntu"


def do_pack():
    '''generates a .tgz archive from the contents
    of the web_static'''

    now = datetime.now()
    filename = "web_static_{}{}{}{}{}{}".format(now.year, now.month,
                                                now.day, now.hour,
                                                now.minute, now.second)
    local("mkdir -p versions")  # create versions folder

    # Compress web_static in .tgz file in moves to versions folder
    com = local(("tar -cvzf versions/{}.tgz web_static").format(filename))

    if com.failed is True:
        return None
    else:
        return ("versions/{}.tgz".format(filename))


def do_deploy(archive_path):
    '''distributes an archive to your web servers'''

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
        return False


def deploy():
    '''creates and distributes an archive to web servers'''

    file_path = do_pack()

    if file_path is None:
        return False

    return do_deploy(file_path)
