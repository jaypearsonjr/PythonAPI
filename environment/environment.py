from environment.appsettings import getConfig

class Environment:
  def __init__(self):
    self.dev = "DEV"
    self.test = "TEST"
    self.prod = "PROD"

def getEnvironment():
    envValue = Environment()
    settings = getConfig()

    match settings.env:
        case "PROD":
            return envValue.prod
        case "TEST":
            return envValue.test
        case _:
            return envValue.dev

"""
TO DO:
    - make env matching more resilient
""" 