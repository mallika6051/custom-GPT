import pdfplumber
from PIL import Image
import pytesseract
from docx import Document

# Function to extract text from images using Tesseract OCR
def extract_text_from_image(image_path):
    # Open the image file
    with Image.open(image_path) as img:
        # Use Tesseract OCR to extract text
        text = pytesseract.image_to_string(img)
        return text

# Function to extract text from PDF containing images
def extract_text_from_pdf_with_images(pdf_path):
    # Open the PDF file
    with pdfplumber.open(pdf_path) as pdf:
        all_text = []
        for page in pdf.pages:
            # Extract images from the page
            images = page.images
            for i, img in enumerate(images):
                # Extract image to a file
                image_path = f"page_{page.page_number}image{i}.png"
                page.to_image(resolution=300).save(image_path, format="PNG")
                # Extract text from the image
                text = extract_text_from_image(image_path)
                # Add extracted text to the list
                all_text.append(text)
        return "\n".join(all_text)

# Extract text from PDF containing images
extracted_text = extract_text_from_pdf_with_images(pdf_file=r'C:\Users\SightSpectrum\PycharmProjects\pythonProject1\39491128 Amendmenttemp0.pdf')

# Save extracted text to a Word document
doc = Document()
doc.add_paragraph(extracted_text)

# Save the Word document
doc.save("extracted_text.docx")
print("Text extracted from PDF and saved to Word document successfully.")
