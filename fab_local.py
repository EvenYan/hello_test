from fabric.api import *
from fabric.contrib.console import confirm

def prepare_deploy():
    local("python3 manage.py makemigrations")
    local("python3 manage.py migrate")
    local("git add . && git commit -m 'init'")
    # 需提前在github创建hello_test仓库
    with settings(warn_only=True):
        result = local("git remote add origin git@github.com:EvenYan/hello_test.git")
    if result.failed and confirm("继续还是中断？"):
        local("git push -u origin master -f")