import os
import re
import PyPDF2
from fpdf import FPDF

class PDFProcessor:
    def __init__(self, pdf_directory, renamed_files = []):
        self.pdf_directory = pdf_directory
        self.renamed_files = renamed_files

    @staticmethod
    def extract_invoice_number(pdf_path):
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()

            pattern = r"Invoice Number: (\w+-\d+-\d+)"
            matches = re.search(pattern, text)
            if matches:
                return matches.group(1)
            else:
                return None

    def process_all_pdfs(self):
        for filename in os.listdir(self.pdf_directory):
            if filename.endswith(".pdf"):
                pdf_path = os.path.join(self.pdf_directory, filename)
                invoice_number = self.extract_invoice_number(pdf_path)
                if invoice_number:
                    renamed_file = self.rename_pdf_with_invoice_number(pdf_path, invoice_number)
                    if renamed_file:
                        self.renamed_files.append(renamed_file)
                else:
                    print(f"No invoice number found in {pdf_path}.")
                    
                    
    @classmethod
    def rename_pdf_with_invoice_number(cls, pdf_path, invoice_number):
        file_name, file_extension = os.path.splitext(pdf_path)
        new_file_name = f"{invoice_number}{file_extension}"
        new_path = os.path.join(os.path.dirname(pdf_path), new_file_name)
        try:
            os.rename(pdf_path, new_path)
            print(f"File {pdf_path} renamed to {new_path} successfully.")
            return (os.path.basename(pdf_path), os.path.basename(new_path))
        except FileNotFoundError:
            print(f"File {pdf_path} not found.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
        return None


    def generate_summary_pdf(self, summary_pdf_path):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(200, 10, txt="PDF Renaming Summary", ln=True, align='C')
        pdf.ln(10)

        pdf.cell(200, 10, txt=f"Total files renamed: {len(self.renamed_files)}", ln=True)
        pdf.ln(10)

        pdf.set_font("Arial", size=10)
        pdf.cell(100, 10, txt="Old Filename", border=1)
        pdf.cell(100, 10, txt="New Filename", border=1)
        pdf.ln()

        for old_name, new_name in self.renamed_files:
            pdf.cell(100, 10, txt=old_name, border=1)
            pdf.cell(100, 10, txt=new_name, border=1)
            pdf.ln()

        pdf.output(summary_pdf_path)
        print(f"Summary PDF generated at {summary_pdf_path}")

class PDFProcessorWithLogging(PDFProcessor):
    def __init__(self, pdf_directory, log_file):
        super().__init__(pdf_directory)
        self.log_file = log_file

    def log_action(self, message):
        with open(self.log_file, 'a') as log:
            log.write(message + '\n')

    def rename_pdf_with_invoice_number(self, pdf_path, invoice_number):
        renamed_file = super().rename_pdf_with_invoice_number(pdf_path, invoice_number)
        if renamed_file:
            self.log_action(f"Renamed: {renamed_file[0]} -> {renamed_file[1]}")
            return renamed_file
        else:
            self.log_action(f"Failed to rename: {pdf_path}")
            return None

if __name__ == "__main__":
    pdf_directory = "./pdfs"
    summary_pdf_path = os.path.join(pdf_directory, "summary.pdf")
    log_file = os.path.join(pdf_directory, "rename_log.txt")

    processor = PDFProcessorWithLogging(pdf_directory, log_file)
    processor.process_all_pdfs()
    processor.generate_summary_pdf(summary_pdf_path)

