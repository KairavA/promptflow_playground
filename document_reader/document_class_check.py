from promptflow.core import tool


@tool
def class_check(file_path: str) -> str:
    print(file_path)
    supported_documents = ["pdf", "docx"]
    matches = [
        intention
        for intention in supported_documents
        if intention in file_path.lower().split(".")[-1]
    ]
    return matches[0] if matches else "unknown"
