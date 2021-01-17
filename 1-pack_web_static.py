#!/usr/bin/python3
"""Fabric script, packing things up"""
import os
from datetime import datetime
import fabric.operations

def do_pack():
    """Generates a .tgz from web_static"""
    fabric.operations.local("mkdir -p versions")
    file_name = "web_static_{}.tgz".format(
        datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"))
    path_ = fabric.operations.local("tar -zcvf versions/{} web_static".format(file_name))
    if path_.failed:
        return None
    return file_name
