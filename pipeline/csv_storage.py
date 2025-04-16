import datetime
import csv
import uuid
from environment.appsettings import getConfig

def cacheResponse(response):
    settings = getConfig()    
    print("Generating output at {location}".format(location=settings.outputPath))

    record = [
        "{id}".format(id=response.id),
        "{output}".format(output=response.choices[0].message.content)]
    
    with open(settings.outputPath, 'at', newline='\n') as file:
        writer = csv.writer(file)
        field = ["id", "output"]
        writer.writerow(record)
        return True

def logResponseRecord(response):
    settings = getConfig()
    print("Generating transaction record at {location}".format(location=settings.recordPath))

    record = ["{id}".format(id=uuid.uuid4()),
                "{resId}".format(resId=response.id),
                "{tokensUsed}".format(tokensUsed=response.usage.total_tokens),
                "{environment}".format(environment=settings.env),
                "{directory}".format(directory=settings.directory),
                "{runDate}".format(runDate=datetime.datetime.now())]
    
    with open(settings.recordPath, 'at', newline='\n') as file:
        writer = csv.writer(file)
        field = ["id", "tokenused", "environment", "directory", "rundate"]
        writer.writerow(record)
        return True
    
"""
TO DO:
    - combine log with cache, both in same call
    - include field row in file
    - add SQLite support
"""