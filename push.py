#!python3
#encoding:utf-8
import time
import os

import schedule
from git import Repo

REPO_DIR = '/opt/Web/'
COMMIT_MESSAGE = 'commit from python script'

def push():
    try:
        REPO_NAMES = os.listdir(REPO_DIR)
        for _repo in REPO_NAMES:
            repo = Repo(REPO_DIR + _repo)
            print(repo)
            if repo.is_dirty():  # 有文件修改
                repo.git.add(update=True)
                repo.index.commit(COMMIT_MESSAGE)
                origin = repo.remote(name='origin')
                print(origin)
                origin.push()
            pass
    except Exception as e:
        print(e)

schedule.every(60).seconds.do(push)
while True:
    schedule.run_pending()
    time.sleep(10)
