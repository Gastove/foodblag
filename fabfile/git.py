# These functions are supposed to support a git deploy process.
# The deploy branch contains generated content; the generated
# content should be committed to a branch, then pushed to github.

from fabric.api import local
from time import strftime, localtime

SOURCE_BRANCH = "master"
DEPLOY_BRANCH = "gh-pages"

def change_branch(branch = "gh-pages"):
    """ Switch to specified Branch """
    local("git branch {}".format(branch))


def commit_all(msg = None):
    """ Commit generated content to branch """
    if not msg:
        timestamp = strftime("%Y-%m-%d %H:%I:$S", localtime())
        msg = "Published Blog at {0}".format(timestamp)
    cmd = "git commit -a -m {0}".format(msg)
    local(cmd)


def merge(merge_target = SOURCE_BRANCH):
    """ Merge target branch into current """
    local("git merge {0}".format(merge_target))


def push(target = DEPLOY_BRANCH):
    """ Push the generated content to the specified target """
    local("git push origin {0}".format(target))
