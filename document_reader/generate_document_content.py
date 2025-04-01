from promptflow.core import tool


@tool
def document_content(pdf_content="", docx_content="") -> str:
    default_response = "Sorry, cannot read document."
    responses = [pdf_content, docx_content]
    return next((response for response in responses if response), default_response)
