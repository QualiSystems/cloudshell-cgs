import os


def find_package_dir(cur_dir=None):
    if cur_dir is None:
        cur_dir = os.path.dirname(__file__)

    if "setup.py" not in os.listdir(cur_dir):
        parent_dir = os.path.dirname(cur_dir)
        find_package_dir(parent_dir)

    return cur_dir


PACKAGE_DIR = find_package_dir()
