from fabric.api import *

def prepare_deploy():
    local("python3 manage.py makemigrations")
    local("python3 manage.py migrate")
    local("git add . && git commit -m 'init'")
    # 需提前在github创建hello_test仓库
    # local("git remote add origin git@github.com:EvenYan/hello_test.git")
    local("git push -u origin master -f")