from promptflow.core import tool
import docx
import os


@tool
def extract_text_from_docx(docx_path):
    """Extracts text from a .docx file."""
    try:
        print(docx_path)
        doc = docx.Document(os.path.join(os.path.dirname(__file__), docx_path))
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        return "\n".join(full_text)
    except FileNotFoundError:
        print("File not found.")
        return None
    except Exception as e:
        print(f"Error processing docx: {e}")
        return None


# Example usage:
# docx_file = "your_document.docx"  # Replace with your docx file path.
# text = extract_text_from_docx(docx_file)
# print(text)
