from fabric.api import *

def prepare_deploy():
    local("python3 manage.py makemigrations")
    local("python3 manage.py migrate")
    local("git add . && git commit -m 'init'")
    local("git push")