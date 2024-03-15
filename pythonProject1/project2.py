import pdfplumber
from PIL import Image
import pytesseract

# Path to your PDF file
# pdf_path = r'C:\Users\SightSpectrum\PycharmProjects\pythonProject1\Amendment Request Version 92603374temp0.pdf'
pdf_file = r'C:\Users\SightSpectrum\PycharmProjects\pythonProject1\39491128 Amendmenttemp0.pdf'
# pdf_file = r'C:\Users\SightSpectrum\PycharmProjects\pythonProject1\64596341 Amendmenttemp0.pdf'
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
extracted_text = extract_text_from_pdf_with_images(pdf_path = r'C:\Users\SightSpectrum\PycharmProjects\pythonProject1\39491128 Amendmenttemp0.pdf')
print(extracted_text)














# Another code

# import fitz  # PyMuPDF
#
# def extract_images_from_pdf(pdf_file):
#     images = []
#     # Open the PDF file
#     pdf_document = fitz.open(pdf_file)
#
#     # Iterate through each page in the PDF
#     for page_number in range(len(pdf_document)):
#         # Load the page
#         page = pdf_document.load_page(page_number)
#
#         # Get the images on the page
#         images_on_page = page.get_images(full=True)
#
#         # Iterate through images on the page
#         for img_info in images_on_page:
#             # Get the XREF of the image
#             xref = img_info[0]
#
#             # Extract the image
#             base_image = pdf_document.extract_image(xref)
#
#             # Append the image to the list
#             images.append(base_image["image"])
#
#     # Close the PDF document
#     pdf_document.close()
#
#     return images
#
# # Path to the PDF file
# pdf_file = r'C:\Users\SightSpectrum\PycharmProjects\pythonProject1\Amendment Request Version 92603374temp0.pdf'
#
# # Extract images from the PDF file
# pdf_images = extract_images_from_pdf(pdf_file)
#
# # Save the images to files
# for i, image in enumerate(pdf_images, 1):
#     image_file_path = f'image_{i}.png'
#     with open(image_file_path, 'wb') as image_file:
#         image_file.write(image)
#         print(f"Image {i} saved to {image_file_path}")
#






