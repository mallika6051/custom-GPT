# from pypdf import PdfReader
# reader = PdfReader(r'C:\Users\SightSpectrum\PycharmProjects\pythonProject1\Amendment Request Version 92603374temp0.pdf')
# print(len(reader.pages))
# page = reader.pages[0]
# print(page.extract_text())

# import fitz  # PyMuPDF
#
# # Open the OCR PDF file
# pdf_file = r'C:\Users\SightSpectrum\PycharmProjects\pythonProject1\Amendment Request Version 92603374temp0.pdf'
# pdf_document = fitz.open(pdf_file)
#
# # Iterate through each page in the PDF
# for page_number in range(len(pdf_document)):
#     page = pdf_document.load_page(page_number)
#
#     # Extract text from the page
#     text = page.get_text()
#
#     # Print the text extracted from the page
#     print(f"Page {page_number + 1}:\n{text}\n")
#
# # Close the PDF document
# pdf_document.close()


# import pdfplumber
#
# # Open the PDF file
# pdf_file = r'C:\Users\SightSpectrum\PycharmProjects\pythonProject1\Amendment Request Version 92603374temp0.pdf'
# with pdfplumber.open(pdf_file) as pdf:
#     # Iterate through each page in the PDF
#     for page_number in range(len(pdf.pages)):
#         page = pdf.pages[page_number]
#
#         # Extract text from the page
#         text = page.extract_text()
#
#         # Print the text extracted from the page
#         print(f"Page {page_number + 1}:\n{text}\n")



from tika import parser

# Parse the PDF file
# pdf_file = r'C:\Users\SightSpectrum\PycharmProjects\pythonProject1\Amendment Request Version 92603374temp0.pdf'
# pdf_file = r'C:\Users\SightSpectrum\PycharmProjects\pythonProject1\39491128 Amendmenttemp0.pdf'
pdf_file = r'C:\Users\SightSpectrum\PycharmProjects\pythonProject1\64596341 Amendmenttemp0.pdf'
parsed_pdf = parser.from_file(pdf_file)

# Extract text from the parsed PDF content
text = parsed_pdf['content']

# Print the extracted text
print(text)



