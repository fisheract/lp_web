from fabric.api import *

env.hosts = ["45.87.3.8"]
env.user = "root"

def test_time():
    run("timedatectl set-timezone 'Asia/Almaty'")
    run("date")
    local("date")