import PyPDF2
import os
import re
from abc import ABC, abstractmethod

class PDFProcessor(ABC):
    def __init__(self, pdf_directory):
        self.pdf_directory = pdf_directory

    @abstractmethod
    def process_pdf(self, pdf_path):
        pass

    def process_all_pdfs(self):
        for filename in os.listdir(self.pdf_directory):
            if filename.endswith(".pdf"):
                pdf_path = os.path.join(self.pdf_directory, filename)
                self.process_pdf(pdf_path)

class InvoicePDFProcessor(PDFProcessor):
    def __init__(self, pdf_directory):
        super().__init__(pdf_directory)

    def extract_invoice_number(self, pdf_path):
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

    def rename_pdf_with_invoice_number(self, pdf_path, invoice_number):
        file_name, file_extension = os.path.splitext(pdf_path)
        new_file_name = f"{invoice_number}{file_extension}"
        new_path = os.path.join(os.path.dirname(pdf_path), new_file_name)
        try:
            os.rename(pdf_path, new_path)
            print(f"File {pdf_path} renamed to {new_path} successfully.")
        except FileNotFoundError:
            print(f"File {pdf_path} not found.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def process_pdf(self, pdf_path):
        invoice_number = self.extract_invoice_number(pdf_path)
        if invoice_number:
            self.rename_pdf_with_invoice_number(pdf_path, invoice_number)
        else:
            print(f"No invoice number found in {pdf_path}.")

if __name__ == "__main__":
    pdf_directory = "./pdfs"
    processor = InvoicePDFProcessor(pdf_directory)
    processor.process_all_pdfs()
