from fabric.api import *
from fabric.contrib.console import confirm

def db():
    local("python3 manage.py makemigrations")
    local("python3 manage.py migrate")
    local("pip freeze > requirements.txt")


def git():
    local("git add . && git commit -m 'init'")


def add_origin():
    with settings(warn_only=True):
        result = local("git remote add origin git@github.com:EvenYan/hello_test.git")
    if result.failed and confirm("继续或中断？"):
        pass

def push():
    result = local("git push -u origin master -f", capture=True)
    print(result)


def prepare_deploy():
    execute(db)
    execute(git)
    execute(add_origin)
    execute(push)