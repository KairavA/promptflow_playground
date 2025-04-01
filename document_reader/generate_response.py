from promptflow.core import tool


@tool
def generate_response(llm_output: str = "") -> str:
    return llm_output
