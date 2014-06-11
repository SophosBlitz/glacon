"""
Self-explaining plugin.
"""
from util import hook
import subprocess
import random
import re

@hook.command
def glacon(inp, input=None):
    p = subprocess.Popen(['git', 'log', '--oneline'], stdout=subprocess.PIPE)
    stdout, _ = p.communicate()
    p.wait()

    revnumber = len(stdout.splitlines())

    shorthash = stdout.split(None, 1)[0]

    latestFeatures = "Support for indexing -EX, -J, -D, and -ARC SCP articles, " + \
        "indexing SCP tales (try !tale), " + \
        "and quote database deletion."
    message = 'I am Glacon 2.0/r%d %s (http://github.com/SophosBlitz/glacon).' \
        % (revnumber, shorthash)

    return message + (' Current new features include: %s' % latestFeatures) + ' Send all bug reports and feature requests to Sophos.'

@hook.command
def source(inp):
    sourceURL = u'http://github.com/SophosBlitz/glacon'
    message = u'My source code is currently hosted on Github at: %s' % sourceURL
    return message
