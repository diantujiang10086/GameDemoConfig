import os
import sys
import config
from gitRepository import GitRepository

path : str
gitHash : str

def updateUnity(configHash, names):
    git = GitRepository(config.unity)
    for path in git.getUpdatePaths():
        name = os.path.basename(path).split('.')[0]
        if name in names or name.replace("Loader","") in names:
            git.add(path)
            pass
    
    git.push('配置修改: ' + configHash)
    gitHash = git.getLastLog('%s')
    print('unity update: '+ gitHash)
    pass

if __name__ == "__main__":
    commit = sys.argv[1]
    
    print("拉取unity目录")
    if not GitRepository(config.unity).pull():
        print('请先解决冲突：'+ config.unity)
        exit()

    print("拉取配置目录")
    git = GitRepository(os.getcwd())
    if not git.pull():
        print('请先解决冲突：'+ git.path)
        exit()

    print("检查配置修改")
    for path in git.getUpdatePaths():
        if path.endswith('.csv') or path.endswith('.xlsx') or path.endswith('.txt'):
            git.add(path)

    if len(git.addPath) > 0:
        names = git.getAddPathNames()
        git.push(commit)
        gitHash = git.getLastLog('%s %H')
        print('update: '+ gitHash)
        updateUnity(gitHash, names)
