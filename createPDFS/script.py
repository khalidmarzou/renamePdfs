import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Function to create an invoice PDF
def create_invoice(pdf_path, invoice_number):
    c = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter
    
    # Set title and metadata
    c.setTitle("Invoice")
    
    # Company Information
    c.setFont("Helvetica-Bold", 20)
    c.drawString(30, height - 50, "Tech Supplies Inc.")
    c.setFont("Helvetica", 12)
    c.drawString(30, height - 70, "1234 Technology Drive")
    c.drawString(30, height - 85, "Innovate City, TX 78901")
    c.drawString(30, height - 100, "Phone: (123) 456-7890")
    c.drawString(30, height - 115, "Email: sales@techsuppliesinc.com")
    
    # Invoice Information
    c.setFont("Helvetica-Bold", 16)
    c.drawString(30, height - 150, f"Invoice Number: {invoice_number}")
    c.drawString(30, height - 170, "Invoice Date: May 27, 2024")
    c.drawString(30, height - 190, "Due Date: June 10, 2024")
    
    # Customer Information
    c.setFont("Helvetica-Bold", 14)
    c.drawString(30, height - 230, "Bill To:")
    c.setFont("Helvetica", 12)
    c.drawString(30, height - 245, "Innovate Solutions LLC")
    c.drawString(30, height - 260, "5678 Innovation Lane")
    c.drawString(30, height - 275, "Creative City, CA 90210")
    c.drawString(30, height - 290, "Phone: (987) 654-3210")
    c.drawString(30, height - 305, "Email: accounts@innovatesolutions.com")
    
    # Table Header
    c.setFont("Helvetica-Bold", 12)
    c.drawString(30, height - 340, "Item Description")
    c.drawString(200, height - 340, "Quantity")
    c.drawString(270, height - 340, "Unit Price")
    c.drawString(350, height - 340, "Total")
    
    # Table Content
    items = [
        ("Ultra HD Monitor 27\"", 5, 300.00, 1500.00),
        ("Wireless Keyboard and Mouse", 10, 50.00, 500.00),
        ("High-Speed HDMI Cable 6ft", 20, 10.00, 200.00),
        ("Ergonomic Office Chair", 3, 150.00, 450.00),
        ("External SSD 1TB", 4, 120.00, 480.00)
    ]
    
    y = height - 360
    for item in items:
        c.setFont("Helvetica", 12)
        c.drawString(30, y, item[0])
        c.drawString(200, y, str(item[1]))
        c.drawString(270, y, f"${item[2]:.2f}")
        c.drawString(350, y, f"${item[3]:.2f}")
        y -= 20
    
    # Totals
    c.setFont("Helvetica-Bold", 12)
    c.drawString(270, y-20, "Subtotal:")
    c.drawString(350, y-20, "$3,130.00")
    c.drawString(270, y-40, "Sales Tax (8%):")
    c.drawString(350, y-40, "$250.40")
    c.drawString(270, y-60, "Total Amount Due:")
    c.drawString(350, y-60, "$3,380.40")
    
    # Footer
    c.setFont("Helvetica", 10)
    c.drawString(30, y-100, "Payment Instructions:")
    c.drawString(30, y-115, "Please make the payment to the following account:")
    c.drawString(30, y-130, "Bank: Tech Bank")
    c.drawString(30, y-145, "Account Number: 123456789")
    c.drawString(30, y-160, "Routing Number: 987654321")
    
    c.drawString(30, y-200, "Terms and Conditions:")
    c.drawString(30, y-215, "1. Payment due within 14 days of invoice date.")
    c.drawString(30, y-230, "2. Late payments may be subject to a late fee of 1.5% per month.")
    c.drawString(30, y-245, "3. Returns must be made within 30 days of purchase and are subject to a restocking fee.")
    
    c.drawString(30, y-280, "Thank you for your business!")
    
    c.save()

# Directory to save PDFs
output_dir = "invoices"
os.makedirs(output_dir, exist_ok=True)

# Generate 100 PDFs
for i in range(1, 101):
    invoice_number = f"INV-2024-{i:03d}"
    pdf_filename = os.path.join(output_dir, f"file_{i}.pdf")
    create_invoice(pdf_filename, invoice_number)

print("PDF invoices generated successfully!")
