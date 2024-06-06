import os
from cglib.openAIClient import get_client

model = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo-1106")
DEBUG = os.getenv("DEBUG", "false")
# get the client
client = get_client()
# get the completion
completion = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "system", "content": "You are a helpful programming assistant."},
        {"role": "user", "content": "What is the purpose of recursion ?"},
    ]
)
# print the completion
if DEBUG == "true":
    print(repr(completion))

print(completion.choices[0].message.content)
