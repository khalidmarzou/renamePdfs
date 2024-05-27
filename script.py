import PyPDF2

# Open the PDF file in binary mode
with open('file_100.pdf', 'rb') as file:
    # Create a PDF file reader object
    pdf_reader = PyPDF2.PdfReader(file)
    
    # Iterate through each page of the PDF
    for page_num in range(len(pdf_reader.pages)):
        # Get the text content of the current page
        page = pdf_reader.pages[page_num]  # Changed 'read.pages' to 'pages'
        text = page.extract_text()          # Changed 'extractText()' to 'extract_text()'

        # Print the text content of the current page
        print("Page", page_num + 1)
        print(text)

