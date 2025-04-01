# promptflow/nodes/openai_api_call.py
from promptflow.core import tool
import requests


@tool
def call_openai_api(connection: dict, prompt: str) -> str:
    """Calls the OpenAI API using retrieved connection details."""
    print(connection)
    api_key = connection["api_key"]
    base_url = connection["base_url"]
    headers = {"Authorization": f"Bearer {api_key}"}
    data = """{
        "model": "gpt-4o",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant who is obsessed with knowing the person you are chating with and divert the conversation to a friedly chat."
            },
            {"role": "user", "content": prompt}
        ],
        "temperature": 1
    }"""
    response = requests.post(f"{base_url}/chat/completions", headers=headers, json=data)
    print(response)
    result = response.json()["choices"][0]["message"]["content"].strip()
    print(result)
    return result
