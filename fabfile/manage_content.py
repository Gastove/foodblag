from fabric.api import lcd, local, settings, task
from fabric.utils import puts
from blog_config import INPUT_PATH, OUTPUT_PATH
import git
import os

SETTINGS_FILE = 'blog_config.py'

# Load paths
ABS_DIR_PATH = os.path.dirname(os.path.abspath(__file__))
ABS_ROOT_DIR = os.path.normpath(os.path.join(ABS_DIR_PATH, '../'))
ABS_SETTINGS_FILE = os.path.join(ABS_DIR_PATH, SETTINGS_FILE)
ABS_OUTPUT_PATH = os.path.normpath(os.path.join(ABS_DIR_PATH, OUTPUT_PATH))
ABS_INPUT_PATH = os.path.normpath(os.path.join(ABS_DIR_PATH, INPUT_PATH))


@task(alias = "gen")
def generate(output = None):
    """ Generate static blog content """
    if output:
        cmd = "pelican -s {0} -o {1} {2}".format(ABS_SETTINGS_FILE,
                                                 output, ABS_INPUT_PATH)
    else:
        cmd = "pelican -s {0} {1}".format(ABS_SETTINGS_FILE, ABS_INPUT_PATH)
    local(cmd)


@task
def clean(output = ABS_OUTPUT_PATH):
    """ Remove old content """
    cmd = "rm -r {0}".format(output)
    with settings(warn_ony = True):
        outcome  = local(cmd)
    if outcome.failed:
        puts("Nothing found; probably already deleted.")


@task
def serve(output = ABS_OUTPUT_PATH):
    """ Load generated output in to an HTTP Server """
    with lcd(output):
        local("python -m pelican.server")


@task(alias="start")
def devserve_start():
    """ Run server; reload if output changes  """
    alter_devserver("start")


@task(alias="stop")
def devserve_stop():
    """ Stop the devserver  """
    alter_devserver("stop")


def alter_devserver(arg):
    cmd = "{0}/develop_server.sh {1}".format(ABS_ROOT_DIR, arg)
    local(cmd)


@task
def publish(output = ABS_OUTPUT_PATH):
    """ Publishes the current master branch to GH Pages """
    git.change_branch(git.DEPLOY_BRANCH)
    git.merge(git.SOURCE_BRANCH)
    generate('./')
    git.commit_all()
    git.push()
    git.change_branch(git.SOURCE_BRANCH)
