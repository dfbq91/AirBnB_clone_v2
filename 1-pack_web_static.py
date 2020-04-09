#!/usr/bin/python3
from datetime import datetime
from fabric.api import *


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
