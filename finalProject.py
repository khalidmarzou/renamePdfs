import PyPDF2
import os
import re

def extract_invoice_number(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        
        pattern = r"Motif de l'opération\s*(\w+)"
        matches = re.search(pattern, text)
        if matches:
            return matches.group(1)
        else:
            return None

def rename_pdf_with_invoice_number(pdf_path, invoice_number):
    # Extract file name and extension
    file_name, file_extension = os.path.splitext(pdf_path)
    # Construct new file name with invoice number
    new_file_name = f"{invoice_number}{file_extension}"
    new_path = os.path.join(os.path.dirname(pdf_path), new_file_name)
    try:
        os.rename(pdf_path, new_path)
        print(f"File {pdf_path} renamed to {new_path} successfully.")
    except FileNotFoundError:
        print(f"File {pdf_path} not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Directory containing PDF files
pdf_directory = "./pdfs"

# Iterate through each PDF file in the directory
for filename in os.listdir(pdf_directory):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(pdf_directory, filename)
        invoice_number = extract_invoice_number(pdf_path)
        if invoice_number:
            rename_pdf_with_invoice_number(pdf_path, invoice_number)
        else:
            print(f"No invoice number found in {pdf_path}.")
