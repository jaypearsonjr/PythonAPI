from openai import OpenAI
from environment import appsettings as config

def getClient():
    client = OpenAI()
    return client

def getResponse(client, persona, content):
    settings = config.getConfig()    
    match settings.env:
        case "PROD":
            return client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": persona},
                    {"role": "user", "content": content}]
            )
        case "TEST":
            return None
        case _:
            return None