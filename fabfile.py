import os
import time

from fabric.api import local, lcd, settings
from fabric.utils import puts

# Load settings
from pelicanconf import INPUT_PATH, OUTPUT_PATH
SETTINGS_FILE = pelicanconf.py

# Load paths
ABS_DIR_PATH = os.path.dirname(os.path.abspath(__file__))
ABS_SETTINGS_FILE = os.path.join(ABS_DIR_PATH, SETTINGS_FILE)
ABS_OUTPUT_PATH = os.path.join(ABS_DIR_PATH, OUTPUT_PATH)
ABS_INPUT_PATH = os.path.join(ABS_DIR_PATH, INPUT_PATH)

def test():
    post_name =

def new_post(post_name):
    """ Make a new post """
    if not post_name:
        puts("No post name, hey?")
    now = time.localtime()
    content_folder = "/".join([now.tm_year, now.tm_mon, now.tm_mday])
    new_file_path = ABS_INPUT_PATH + content_folder



def _open_file(filepath):
    """ Open the given file for editing  """
    cmd = "$EDITOR " + filepath
    local(cmd)
