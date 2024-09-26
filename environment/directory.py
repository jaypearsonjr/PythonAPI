import os
from environment.appsettings import getConfig

def getStagingDirectory():
    settings = getConfig()
    wrk = os.getcwd()
    path = settings.directory
    dir =  "{cwd}{prjPath}".format(cwd=wrk, prjPath=path)
    return dir