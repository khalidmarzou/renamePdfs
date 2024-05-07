import os

def rename_pdf(old_path, new_path):
    try:
        os.rename(old_path, new_path)
        print(f"File {old_path} renamed to {new_path} successfully.")
    except FileNotFoundError:
        print(f"File {old_path} not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage:
old_path = "./pdfs/modele_de_facture.pdf"
new_path = "./pdfs/552.pdf"

rename_pdf(old_path, new_path)

