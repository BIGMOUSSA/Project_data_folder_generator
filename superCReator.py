from utils import git_repo_init, create_project_data_path
import os

class SuperFolder :
    
    def __init__(self, mypath) -> None:
        self.mypath = mypath

    def PathCreator(self, method):
        create_project_data_path(self.mypath, method=method)

    def Init(self):
        git_repo_init(self.mypath)

if  __name__ == '__main__':
    os.mkdir("testFolderPath")

    testPath = "testFolderPath"
    DataCreator1 = SuperFolder(testPath)
    DataCreator1.PathCreator(method="os")
    DataCreator1.Init()