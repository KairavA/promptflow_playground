from promptflow.core import tool
import fitz  # PyMuPDF


@tool
def analyze_pdf_fitz(pdf_path):
    """
    Extracts text and checks for images from a PDF file using PyMuPDF.

    Args:
        pdf_path (str): The path to the PDF file.

    Returns:
        tuple: (extracted_text, has_images)
    """
    try:
        doc = fitz.open(pdf_path)
        all_text = []
        all_images = []
        for page in doc:
            all_text.append(page.get_text())
            all_images.append(page.get_images(full=True))

        doc.close()
        print(all_text[:100])
        return "\n".join(all_text)

    except Exception as e:
        print(f"Error processing PDF: {e}")
        return None


# # Example PDF usage:
# pdf_text, pdf_images = analyze_pdf_fitz("WK3-GE-MC3-PVintro.pdf")
# if pdf_text:
#     print("PDF Text:\n", "\n".join(pdf_text))
# if pdf_images:
#     print("PDF contains images.", len(pdf_images))
#     # print(pdf_images)
# else:
#     print("PDF does not contain images.")
