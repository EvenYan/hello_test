from fabric.api import *

env.user='root'
# env.host='172.16.2.142'
env.hosts=['172.16.2.142']
env.user="root"
env.exclude_hosts=['192.168.1.21','192.168.1.22']
env.password='!web123@'
env.port="22"
env.passwords={
    'root@172.16.2.142':'!web123@'
}

def linux():
    run("uname -a")