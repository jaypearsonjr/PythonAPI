from openai import OpenAI
from unittest.mock import MagicMock

# environment
class Environment:
  def __init__(self):
    self.dev = "DEV"
    self.test = "TEST"
    self.prod = "PROD"
envValue = Environment()
env = envValue.dev

# test object
def get_mock_openai_client():
    # Create a mock object for the OpenAI client
    mock_openai = MagicMock()

    # Simulate the OpenAI completion endpoint behavior
    mock_completion = MagicMock()
    mock_completion.create.return_value = {
        "id": "chatcmpl-abc123",
        "object": "chat.completion",
        "created": 1677858242,
        "model": "gpt-4o-mini",
        "usage": {
            "prompt_tokens": 13,
            "completion_tokens": 7,
            "total_tokens": 20,
            "completion_tokens_details": {
                "reasoning_tokens": 0
            }
        },
        "choices": [
            {
                "message": {
                    "role": "assistant",
                    "content": "\n\nThis is a test!"
                },
                "logprobs": None,
                "finish_reason": "stop",
                "index": 0
            }
        ]
    }

    # Attach the mock completion object to the mock OpenAI client
    mock_openai.Completion = mock_completion

    # Return the mock client
    return mock_openai

# methods
def getClient():
    client = OpenAI()
    return client

def getResponse(client, role, content):
    
    match env:
        case envValue.prod:
            return client.chat.responses.create(
                model="gpt-4o-mini",
                messages=[{"role": role, "content": content}]
            )
        case envValue.dev:
            return get_mock_openai_client()
        case _:
            return get_mock_openai_client()

def printResponse(response):
    print('--- BEGIN ------------------------------')
    print("Response: " + response.id)
    print('---------------------------------')
    print("Mesage: " + response.choices[0].message)
    print('---------------------------------')
    print("Content: " + response.choices[0].message.content)
    print('---------------------------------')
    print("Cost: " + response.usage.total_tokens)
    print('--- END ------------------------------')

def cacheResponse(response):
    print("response cached")

def createResponseRecord(responseId):
    print("repsone record created")

# business logic
client = getClient()
response = getResponse(client=client, role="user", content="Hi.")

# results
printResponse(response=response)