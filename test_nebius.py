import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("NEBIUS_API_KEY")
model = os.getenv("NEBIUS_MODEL")

if not api_key or not model:
    raise ValueError("API key or model is missing from .env")

client = OpenAI(
    base_url="https://api.tokenfactory.nebius.com/v1/",
    api_key=api_key
)

response = client.chat.completions.create(
    model=model,
    messages=[
        {
            "role": "user",
            "content": "Say: Nebius connection successful"
        }
    ],
    max_tokens=50
)

print("Nebius response:")
print(response.choices[0].message.content)