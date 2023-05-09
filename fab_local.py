from fabric.api import *
from fabric.contrib.console import confirm


env.user='root'
# env.host='172.16.2.142'
env.hosts=['172.16.2.142', "172.16.2.141"]
env.exclude_hosts=['172.16.2.141']
env.password='!web123@'
env.port="22"
env.passwords={
    'root@172.16.2.142':'!web123@',
    'normal@172.16.2.132':'abc',
}

def db():
    local("python3 manage.py makemigrations")
    local("python3 manage.py migrate")
    # local("pip freeze > requirements.txt")


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

def pull():
    with cd("/root"):
        run("git clone git@github.com:EvenYan/hello_test.git")

def runserver():
    with cd("/root/hello_test"):
        run("pip install -r requirements.txt")
        run("python3 manage.py runserver")


def prepare_deploy():
    execute(db)
    execute(git)
    execute(add_origin)
    execute(push)


def deploy():
    execute(pull)
    execute(runserver)