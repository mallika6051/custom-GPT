import PyPDF2
import csv

def pdf_to_csv(pdf_path, csv_path):
    # Open the PDF file
    with open(pdf_path, 'rb') as pdf_file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Initialize an empty string to store extracted text
        pdf_text = ""

        # Iterate through all pages and extract text
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_text += page.extract_text()

    # Split the text into lines
    lines = pdf_text.split('\n')

    # Create a CSV file and write the lines into it
    with open(csv_path, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)

        for line in lines:
            # Split each line into columns based on a delimiter (e.g., comma)
            # Adjust the delimiter based on the structure of your PDF
            columns = line.split(',')

            # Write the columns into the CSV file
            csv_writer.writerow(columns)

if __name__ == "__main__":
    # Specify the paths for your PDF and CSV files
    input_pdf_path = 'C:\\Users\\SightSpectrum\\PycharmProjects\\converting\\ARE.pdf'
    output_csv_path = 'C:\\Users\\SightSpectrum\\PycharmProjects\\converting\\output.csv'

    # Convert PDF to CSV
    pdf_to_csv(input_pdf_path, output_csv_path)





import fitz  # PyMuPDF

def pdf_to_csv(input_pdf_path, output_csv_path):
    doc = fitz.open(input_pdf_path)

    # Define the page region to exclude for header and footer
    header_region = (0, 0, doc[0].rect.width, 100)  # Adjust the height accordingly
    footer_region = (0, doc[0].rect.height - 100, doc[0].rect.width, doc[0].rect.height)  # Adjust the height accordingly

    with open(output_csv_path, 'wb') as csv_file:  # Use 'wb' for binary mode
        for page_num in range(doc.page_count):
            page = doc[page_num]

            # Extract text from the entire page
            text = page.get_text()

            # Exclude header and footer regions
            header_text = page.get_text("text", clip=header_region)
            footer_text = page.get_text("text", clip=footer_region)
            text = text.replace(header_text, '').replace(footer_text, '')

            # Write the processed text to the CSV file
            csv_file.write(text.encode('utf-8'))

    doc.close()

if __name__ == "__main__":
    input_pdf_path = 'C:\\Users\\SightSpectrum\\PycharmProjects\\converting\\ARE.pdf'
    output_csv_path = 'C:\\Users\\SightSpectrum\\PycharmProjects\\converting\\output1.csv'
    pdf_to_csv(input_pdf_path, output_csv_path)
