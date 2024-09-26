from chat.openai_client import *
from environment.directory import *
from pipeline.csv_storage import *

"""
startup
"""
# environment, current working dir, established in appsettings during client creation
"""
business logic
"""
# create client
print("Starting client ...")
client = getClient()
# submit response
print("Submitting request ...")
response = getResponse(client=client, persona="I am a usefull assistant.", content="Hi.")
# generate response file
print("Caching response ...")
cacheResponse(response=response)
# generate transaction record
print("Logging transaction details ...")
logResponseRecord(response=response)
# end
print("Job comleted.")


""" 
TO DO:
    - pass in persona and content
    - 
"""