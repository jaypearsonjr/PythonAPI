from chat import openai_client as request
from environment.directory import *
from pipeline import csv_storage as csv
from personas.character import Character

"""
startup
"""
# environment, current working dir, established in appsettings during client creation
# persona
character = Character("philospher")
query = "Do we have free will?"
print(character.persona)
print(query)


"""
business logic
"""
# create client
print("Starting client ...")
client = request.getClient()

# submit response
print("Submitting request ...")
response = request.getResponse(client=client, persona=character.persona.description, content=query)

# generate response file
print("Caching response ...")
csv.cacheResponse(response=response)

# generate transaction record
print("Logging transaction details ...")
csv.logResponseRecord(response=response)

# end
print("Job completed.")


""" 
TO DO:
    - pass in persona and content
    - model options to select from
    - select from pre-made personas, like characters to talk to
        *health coach
        *techbro
        *
    - add file columns: sumbitedBy
    - ability to check cached responses first
    - ability to resubmit previous request 
"""