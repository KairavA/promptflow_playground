from promptflow.client import PFClient
from get_connection import get_connection
from radai_api_call import call_openai_api

# con = get_connection("", "")
# result = call_openai_api(con, "tell me a joke")
# print(result)

client = PFClient()

# Define the inputs to your flow
inputs = {"user_prompt": "tell me a joke"}

# Run the flow
result = client.test(flow=".", inputs=inputs)

# Print the results
print(result)
