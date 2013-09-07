import os
from time import localtime, strftime
import re

from fabric.api import local, lcd, settings
from pelicanconf import INPUT_PATH, OUTPUT_PATH
from fabric.utils import puts

SETTINGS_FILE = 'pelicanconf'

# Load paths
ABS_DIR_PATH = os.path.dirname(os.path.abspath(__file__))
ABS_SETTINGS_FILE = os.path.join(ABS_DIR_PATH, SETTINGS_FILE)
ABS_OUTPUT_PATH = os.path.join(ABS_DIR_PATH, OUTPUT_PATH)
ABS_INPUT_PATH = os.path.join(ABS_DIR_PATH, INPUT_PATH)

def test():
    name = "Three Singing Pigs! Love; Romance"
    new_post(name)


def new_post(name = "", extension = ".md", should_open = True):
    """ Make a new post """
    if not name:
        puts("Enter a post name:")
        name = raw_input("\t:")
    path = _post_path()
    file_name = _post_name(name) + extension
    full_post_uri = os.path.join(path, file_name)
    # Function to check if post already exists goes here.
    puts("Generated new post: ", file_name)
    puts("Stored it in: ", path)
    puts("Adding default metadata")
    _write_default_metadata(name, full_post_uri)
    if should_open:
        puts("Opening new post")
        _open_file(full_post_uri)
    else:
        puts("Complete.")


def _write_default_metadata(post_real_name, post_full_path):
    # Control structure for metadata order
    def load_config_or_else(key, default):
        """ Try to load a value from config; if not found, return default  """
        try:
            val = getattr(__import__(SETTINGS_FILE, key.upper()), key.upper())
            return val
        except AttributeError:
            return default

    metadata_keys = [
        "Title", "Author", "Date", "Slug", "Category", "Tags", "Summary"
    ]
    metadata_defaults = {
        "Title": post_real_name,
        "Date": strftime("%Y-%m-%d", localtime()),
        "Category": "",
        "Tags": "",
        "Slug": os.path.basename(post_full_path[:-3]),
        "Author": "",
        "Summary": ""
    }
    for key in metadata_keys:
        metadata_defaults[key] = load_config_or_else(key, metadata_defaults[key])

    with open(post_full_path, 'w') as pointer:
        for key in metadata_keys:
            pointer.write("%s: %s\n" % (key, metadata_defaults[key]))


def _post_path():
    """ Generate the correct post path and make sure it exists  """
    date_string_pieces = strftime("%Y,%m,%d", localtime()).split(",")
    path = "/".join(date_string_pieces)
    abs_path = os.path.join(ABS_INPUT_PATH, path)
    if not os.path.exists(abs_path):
        local("mkdir -p %s" % abs_path)
    return abs_path


def _post_name(input_string):
    """ Generate a valid post name  """
    def is_empty(entry): return True if entry else False
    first_pass = re.sub("\s", "_", input_string.lower())
    second_pass = "".join(filter(empty, re.findall("\w", first_pass)))
    third_pass = re.search("([a-z0-9]*_){,4}[a-z0-9]*", second_pass).group()
    timestamp = strftime("%Y-%m-%d", localtime())
    return "_".join([timestamp, third_pass])


def _open_file(filepath):
    """ Open the given file for editing  """
    cmd = "$EDITOR " + filepath
    local(cmd)
