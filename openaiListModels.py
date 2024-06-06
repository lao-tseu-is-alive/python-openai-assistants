# Description: List all the models available in OpenAI
from cglib.openAIClient import get_client

# get the client
client = get_client()
models = client.models.list()
# list all models
for model in models:
    print(repr(model))
