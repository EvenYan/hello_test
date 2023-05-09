from fabric.api import *
from fabric.contrib.console import confirm

def db():
    local("python3 manage.py makemigrations")
    local("python3 manage.py migrate")


def git():
    local("git add . && git commit -m 'init'")

@runs_once
def add_origin():
    local("git remote add origin git@github.com:EvenYan/hello_test.git")


def push():
    result = local("git push -u origin master -f", capture=True)
    print(result)


def prepare_deploy():
    execute(db)
    execute(git)
    # execute(add_origin)
    execute(push)