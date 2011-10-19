#!/usr/bin/env python

from fabric.api import local

from glob import glob
import os
from subprocess import Popen


def ls():
    for f in glob('*'):
        f = os.path.abspath(f)
        print f

def save(comment):
    local('git commit -a -m "{0}"'.format(comment))
    local('git pull --rebase')
    local('git push')

def push():
    local('git push')

def pull():
    local('git pull --rebase')

def status():
    local('git status')

def clean():
    for f in glob('*.html'):
        f = os.path.abspath(f)
        local('rm {0}'.format(f))


def build():
    for f in glob('*'):
        if f.endswith('.py'): continue
        f = os.path.abspath(f)
        out = f + ".html"
        print f, out
        local('rst2html.py %s %s' % (f, out))


