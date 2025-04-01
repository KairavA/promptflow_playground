import requests
import dotenv

dotenv.load_dotenv()


def store_connection_details(service_name, username, details):
    """Stores connection details in the keyring."""
    keyring.set_password(
        service_name, username, str(details)
    )  # Store details as a string (e.g., JSON)


# Example: Store OpenAI connection details
openai_details = {
    "api_key": "eyJraWQiOiJ0VVgxTHJzSlRJcjNnVktBbjhQVlZwWTdXaTZsWW82SURjemZCNGxNQy1VIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULjhBUmZLcGdNR0VfSkVKc09ucVUyV3pwVnZKZmROZ2tYOG1aVktXOWR5c3MiLCJpc3MiOiJodHRwczovL2VhdG9udmFuY2V1YXQub2t0YXByZXZpZXcuY29tL29hdXRoMi9hdXMyY252Y2VtYkNxdEdncjBoOCIsImF1ZCI6InJhZGl1c2FpLXNlcnZpY2UiLCJpYXQiOjE3NDI4MjAyNzMsImV4cCI6MTc0MjgyMzg3MywiY2lkIjoiMG9hMmNudTFzbzF2SFM1aU4waDgiLCJzY3AiOlsiUkFESVVTQUlfQ09NUExFVElPTiJdLCJzdWIiOiIwb2EyY251MXNvMXZIUzVpTjBoOCJ9.bFQI7PNff1IH0eFUldP5W6jbL5U84FyGpfADKQgh9eu53pd1nhCB2qJ2mZIL81ZMiVWLVI18XMbUF-04DAUBpqIzhof8wYZNKdk1Meb6zlynQlUkOyGjRt5ZytFgLHBgVW4fv6qaohSglguUEOR7NqAKhC0-4q3ZQ1boT4sbNy-YkQYQtsdTKx1srDffOCEBmIhFpKCQu9exMjuu5h-4blHC2xta7SR5M54zMGUGrir7A1ygxMC9g6zAWP4UwcHV1pGfipUXYsGbp0yjOaDhlsVuM4DbcTiRcc_sZkuPtdYkSKj3yHDRbDD5aYzLbITN2RZgC66dQyKNeX6mitobHQ",
    "base_url": "https://radai.uat.genai.use1.aws.paraport.com/v1",
}
# store_connection_details("my_prompt_flow", "openai_connection", openai_details)


# promptflow/nodes/get_connection.py
def get_connection(service_name: str, username: str) -> dict:
    """Retrieves connection details from the keyring."""
    # details_str = keyring.get_password(service_name, username)
    # return json.loads(details_str)
    return openai_details


# promptflow/nodes/openai_api_call.py
def call_openai_api(connection: dict, prompt: str) -> str:
    """Calls the OpenAI API using retrieved connection details."""
    api_key = connection["api_key"]
    base_url = connection["base_url"]
    headers = {"Authorization": f"Bearer {api_key}"}
    data = {"prompt": prompt, "max_tokens": 150}  # example data
    response = requests.post(f"{base_url}/completions", headers=headers, json=data)
    return response.json()["choices"][0]["text"].strip()
