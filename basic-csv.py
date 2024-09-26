import os
import datetime
import csv
import uuid
from openai import OpenAI

# environment
class Environment:
  def __init__(self):
    self.dev = "DEV"
    self.test = "TEST"
    self.prod = "PROD"

envValue = Environment()
env = envValue.prod

#current working directory
wrk = os.getcwd()
path = "\\data"
dir =  "{cwd}{prjPath}".format(cwd=wrk, prjPath=path)

# mock object

# methods
def getClient():
    client = OpenAI()
    return client
def getResponse(client, persona, content):
    
    match env:
        case envValue.prod:
            return client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": persona},
                    {"role": "user", "content": content}]
            )
        case envValue.dev:
            return None
        case _:
            return None
def printResponse(response):
    print('--- BEGIN ------------------------------')
    print("Response: ")
    print(response.id)
    print('---------------------------------')
    print("Mesage: ")
    print(response.choices[0].message)
    print('---------------------------------')
    print("Content: ")
    print(response.choices[0].message.content)
    print('---------------------------------')
    print("Cost: ")
    print(response.usage.total_tokens)
    print('--- END ------------------------------')
def cacheResponse(response):
    print("response cached")
def createResponseRecord(responseId):
    print("repsone record created")

# business logic
# create client
print("Starting client ...")
client = getClient()

# submit response
print("Submitting request ...")
response = getResponse(client=client, persona="I am a usefull assistant.", content="Hi.")

# print results
print("RESPONSE: ")
printResponse(response=response)

#generate response file
responseFile = dir + "\\outputs.csv"
print("Generating output record at {location}".format(location=responseFile))
resRecord = [
    "{id}".format(id=response.id),
    "{output}".format(output=response.choices[0].message.content)]
with open(responseFile, 'at', newline='\n') as file:
    writer = csv.writer(file)
    field = ["id", "output"]
    writer.writerow(resRecord)

#generate transaction record
tranFile = dir + "\\transactions.csv"
print("Generating transaction record at {location}".format(location=tranFile))
tranRecord = ["{id}".format(id=uuid.uuid4()),
              "{resId}".format(resId=response.id),
              "{tokensUsed}".format(tokensUsed=response.usage.total_tokens),
              "{environment}".format(environment=env),
              "{directory}".format(directory=dir),
              "{runDate}".format(runDate=datetime.datetime.now())]
with open(tranFile, 'at', newline='\n') as file:
    writer = csv.writer(file)
    field = ["id", "tokenused"]
    writer.writerow(tranRecord)

# end
print("Job comleted.")