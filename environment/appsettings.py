import os
from configparser import ConfigParser

class appsettings():
    def __init__(self) -> None:
        self.env = ""
        self.directory = ""
        self.outputName = ""
        self.recordName = ""
        self.outputPath = ""
        self.recordPath = ""

def getConfig():
    config = ConfigParser()
    configPath = "config.ini"

    dirname = os.getcwd()
    filename = os.path.join(dirname, configPath)
    print(filename)
    config.read(filename)

    settings = appsettings()
    settings.env = config.get('main', 'environment')
    settings.directory = config.get('main', 'outputPath')
    settings.outputName = config.get('main', 'outputFile')
    settings.recordName = config.get('main', 'recordFile')
    settings.outputPath = dirname + settings.directory + settings.outputName
    settings.recordPath = dirname + settings.directory + settings.recordName

    return settings


