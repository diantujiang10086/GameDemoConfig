import os

try:
    from git import Repo
except:
    os.system('pip install gitpython')    
    from git import Repo
    
class GitRepository(object):
    def __init__(self, path) -> None:
        repo = Repo(path)
        self.path = path
        self.git = repo.git
        self.addPath = []
        pass

    def add(self, path):
        print("add: " + path)
        self.addPath.append(path)
        self.git.add(path)

    def getAddPathNames(self):
        result=[]
        for path in self.addPath:
            name = os.path.basename(path).split('.')[0]
            if name not in result:
                result.append(name)
        return result

    def push(self, msg):
        self.git.commit('-m ' + msg)
        self.git.push()
        self.addPath = []

    def pull(self):
        try:
            self.git.pull()
            return True
        except Exception as ex:
            print(ex)
            return False

    def getUpdatePaths(self):
        result = self.git.diff('--name-only').split('\n')
        status = self.git.status('-s')
        for item in status.split('\n'):
            if '??' in item:
                result.append(item.replace('?? ',''))
        return result

    def commit(self, msg):
        self.git.commit('-m ' + msg)
    
    def getLastLog(self, _format):
        lastHash = self.git.log('--pretty=format:"{0}"'.format(_format), max_count = 1)
        return lastHash.replace('"','')