# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from promptflow.core import tool
import fitz  # PyMuPDF

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need


@tool
def my_python_tool(input1: str) -> str:
    return "Prompt: " + input1


# @tool
# def analyze_pdf_fitz(pdf_path):
#     """
#     Extracts text and checks for images from a PDF file using PyMuPDF.

#     Args:
#         pdf_path (str): The path to the PDF file.

#     Returns:
#         tuple: (extracted_text, has_images)
#     """
#     try:
#         doc = fitz.open(pdf_path)
#         all_text = []
#         all_images = []
#         for page in doc:
#             all_text.append(page.get_text())
#             all_images.append(page.get_images(full=True))

#         doc.close()
#         return all_text, all_images

#     except Exception as e:
#         print(f"Error processing PDF: {e}")
#         return None, False


# # Example PDF usage:
# pdf_text, pdf_images = analyze_pdf_fitz("WK3-GE-MC3-PVintro.pdf")
# if pdf_text:
#     print("PDF Text:\n", "\n".join(pdf_text))
# if pdf_images:
#     print("PDF contains images.", len(pdf_images))
#     # print(pdf_images)
# else:
#     print("PDF does not contain images.")
