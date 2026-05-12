import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

client = AzureOpenAI(
    api_key=os.environ["PROJECT_API_KEY"]
    api_version="2024-12-01-preview",
    azure_endpoint= os.environ["PROJECT_ENDPOINT"]
)

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {
            "role": "system",
            "content": "Você é um assistente útil. Responda em português."
        },
        {
            "role": "user",
            "content": "Como realizo tais testes? Responda em uma frase."
        }
    ]
)

print(response.choices[0].message.content)