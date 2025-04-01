# promptflow/nodes/openai_api_call.py
from promptflow.core import tool
import logging
from openai import OpenAI


@tool
# def call_openai_api(connection: dict, prompt: str) -> str:
def call_openai_api(
    system_prompt: str, summary_prompt: str, document_class: str
) -> str:
    """Calls the OpenAI API using retrieved connection details."""
    if document_class == "unknown":
        return "Unable to read file"

    connection = {
        "api_key": "eyJraWQiOiI3RVljV2sxX1UyWXdWWTh4Y19feDFWQ3hhR3dWMlVyRDYxMGhrZWh2amZjIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULjEwTUtkRUg3a1B4N2p6dEZDWm13a1JES3VzTF9PMzh3WFJPWUJCWEZ6akUiLCJpc3MiOiJodHRwczovL2VhdG9udmFuY2VkZXYub2t0YXByZXZpZXcuY29tL29hdXRoMi9hdXMyOHMxaDh0NTk5NXMzajBoOCIsImF1ZCI6InJhZGl1c2FpLXNlcnZpY2UiLCJpYXQiOjE3NDMxNzMzOTEsImV4cCI6MTc0MzE3Njk5MSwiY2lkIjoiMG9hMjhzMXljandzTW1qY0UwaDgiLCJzY3AiOlsiUkFESVVTQUlfQ09NUExFVElPTiJdLCJzdWIiOiIwb2EyOHMxeWNqd3NNbWpjRTBoOCJ9.Aqzp-fNQBwi6PzinuQC3EYpwzwzI63PcIc3cXzSreMgt2UXhrhxl3FpZGQLuXHvSrrb9Hzm_wSLvjiaxYu0o7R2V5A8MHN2qozPHV7q49KUYr-0AkpClAfeCyXHVaSKeCWcoP9g9gcRMT1OgDKRc5FcosItdz9dcNWP3seknGAOGQV_UIlKm7SRLt7j6OHGAvM9PDCEK3XRO1M8TtZle58YZa29XXu5tJxfiCDhT5BcZc-Fhqp32UxV8rjnzT7UYuHmdxAou0GBcizS-U2GZ0FzlhhwSmBhWPlOAVXqY7VeHpajCijhJiim6ad3jyLMvIJ9sXjTFf4luC-LF5ZI88Q",
        "base_url": "https://radai-dev.sandbox.genai.use1.aws.paraport.com/v1",
    }
    logging.info(connection)
    api_key = connection["api_key"]
    base_url = connection["base_url"]
    model = "gpt-4o"
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": summary_prompt},
    ]
    client = OpenAI(api_key=api_key, base_url=base_url)
    completion = client.chat.completions.create(
        model=model, messages=messages, temperature=1
    )

    logging.info(completion)
    output = completion.choices[0].message.content.strip()
    # headers = {"Authorization": f"Bearer {api_key}"}
    # data = {
    #     "model": "gpt-4o",
    #     "messages": [
    #         {"role": "system", "content": system_prompt},
    #         {"role": "user", "content": summary_prompt},
    #     ],
    #     "temperature": 1,
    # }
    # data = json.dumps(data)
    # response = requests.post(f"{base_url}/chat/completions", headers=headers, json=data)
    # print(response)
    # result = response.json()["choices"][0]["message"]["content"].strip()

    logging.info(output)
    return output
