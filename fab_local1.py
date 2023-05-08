from fabric.api import *


def db():
    local("python3 manage.py makemigrations")
    local("python3 manage.py migrate")

def commit():
    local("git add . && git commit -m 'init'")

def push():
    # 需提前在github创建hello_test仓库
    # 第一次需要添加远程分支
    # local("git remote add origin git@github.com:EvenYan/hello_test.git")
    local("git push -u origin master -f")

def prepare_deploy():
    db()
    commit()
    push()
    
    
    