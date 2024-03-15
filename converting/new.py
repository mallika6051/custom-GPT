# import PyPDF2
#
# def print_text_from_pdf(input_pdf, lines_to_remove):
#     with open(input_pdf, 'rb') as file:
#         pdf_reader = PyPDF2.PdfReader(file)
#
#         # Initialize variables to store modified lines
#         merged_lines = {}
#
#         for page_number in range(len(pdf_reader.pages)):
#             page = pdf_reader.pages[page_number]
#             text = page.extract_text()
#
#             # Split text into lines
#             lines = text.split('\n')
#
#             # Perform specific line manipulations
#             for i in range(len(lines)):
#                 # Merge lines 63 to 64, 94 to 95, 101 to 102, 214 to 215
#                 if i in [63, 94, 101, 214]:
#                     merged_lines[i] = lines[i] + ' ' + lines[i + 1]
#
#                 # Remove lines 123 to 126
#                 elif i in range(123, 127):
#                     lines[i] = ''
#
#             # Remove empty lines after line manipulations
#             lines = [line for line in lines if line]
#
#             # Print each line excluding specified lines
#             for line_index, line_content in enumerate(lines):
#                 if line_index not in lines_to_remove:
#                     print(f"Line {line_index}:\n{line_content}")
#
#         # Print merged lines
#         for index, content in merged_lines.items():
#             print(f"Merged Line {index} and {index + 1}:\n{content}")
#
# # Example usage
# input_pdf_file = 'ARE.pdf'
#
# # Get the total number of lines in the document
# with open(input_pdf_file, 'rb') as file:
#     pdf_reader = PyPDF2.PdfReader(file)
#     total_lines = sum(len(page.extract_text().split('\n')) for page in pdf_reader.pages)
#
# # Define the lines to remove (from index 0 to 7 and from 239 to the end)
# lines_to_remove = list(range(8)) + list(range(239, total_lines))
#
# # Call the function
# print_text_from_pdf(input_pdf_file, lines_to_remove)
#

















# import pdfplumber
# import csv
# import os
# import re
#
# # Specify the directory where you want to save the CSV file
# output_directory = 'C:\\Users\\SightSpectrum\\PycharmProjects\\converting'
# # Ensure the directory exists, or create it if it doesn't
# os.makedirs(output_directory, exist_ok=True)
# # Specify the full path for the CSV file
# csv_file = os.path.join(output_directory, "Final.csv")
# # Create a list to store descriptions and their corresponding values
# data = []
# year = '2023'
# # Specify the PDF file path
# pdf_file = 'C:\\Users\\SightSpectrum\\PycharmProjects\\converting\\ARE.pdf'  # Replace with your PDF file path
#
# # Open the PDF file for text extraction
# with pdfplumber.open(pdf_file) as pdf:
#     text = ""  # Initialize the 'text' variable
#
#     # Iterate through the specified pages
#     for page_number in range(len(pdf.pages)):
#         page = pdf.pages[page_number]  # Adjust page numbering (0-based to 1-based)
#         text += page.extract_text()
#
#     # print(text)
#     entries = text.split('\n')
#
#     # Initialize the Country variable outside the loop
#     Country = ''
#
#     # Iterate through each entry on the page
#     for i, entry in enumerate(entries, start=1):
#         key_values = entry.split()
#
#         if i == 3:
#             Country = str(key_values[0])
#
#         phrases_to_find = ["Basic Needs", "Foundations of Wellbeing", "Opportunity"]
#         for phrase in phrases_to_find:
#             # phrase_match = re.search(phrase + r'\s+(\d+\.\d+)', parsed_text)
#             phrase_match = re.search(phrase + r'\s+(\d+\.\d+)\s+(\d+)', text)
#             if phrase_match:
#                 Str_value = phrase_match.group(1)
#                 Str_Rank = phrase_match.group(2)
#                 Str_Ind = phrase
#                 # Country_Name=get_country(pdf_path)
#                 # print(Str_Ind)
#                 # print(Str_value)
#                 # print(Str_Rank)
#                 # print(Country_Name)
#                 data.append((year, Country, Str_Ind, Str_value, Str_Rank))
#             else:
#                 print(f"Phrase '{phrase}' not found.")
#                 Str_value = ''
#                 Str_Rank = ''
#                 Str_Ind = phrase
#                 data.append((year, Country, Str_Ind, Str_value, Str_Rank))
#
# # Write data to CSV
# with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(['YEAR', 'COUNTRY', 'IND_CODE', 'SCORE', 'RANK'])  # Write header
#     writer.writerows(data)  # Write data rows
#
# print('Completed...')

















import pdfplumber
import csv
import os
import re

# Specify the directory where you want to save the CSV file
output_directory = 'C:\\Users\\SightSpectrum\\PycharmProjects\\converting'
# Ensure the directory exists, or create it if it doesn't
os.makedirs(output_directory, exist_ok=True)
# Specify the full path for the CSV file
csv_file = os.path.join(output_directory, "Final.csv")
# Create a list to store descriptions and their corresponding values
data = []
year = '2023'
# Specify the PDF file path
pdf_file = 'C:\\Users\\SightSpectrum\\PycharmProjects\\converting\\ARE.pdf'  # Replace with your PDF file path

# Open the PDF file for text extraction
with pdfplumber.open(pdf_file) as pdf:
    text = ""  # Initialize the 'text' variable

    # Iterate through the specified pages
    for page_number in range(len(pdf.pages)):
        page = pdf.pages[page_number]  # Adjust page numbering (0-based to 1-based)
        text += page.extract_text()

    # Extract column names (Basic Needs, Foundations of Wellbeing, Opportunity)
    column_names_match = re.search(
        r'(Basic Needs)\s+(\d+\.\d+)\s+(\d+)\s+(Foundations of Wellbeing)\s+(\d+\.\d+)\s+(\d+)\s+(Opportunity)\s+(\d+\.\d+)\s+(\d+)',
        text)
    if column_names_match:
        basic_needs = column_names_match.group(1)
        foundations_of_wellbeing = column_names_match.group(4)
        opportunity = column_names_match.group(7)

        # Write header to CSV
        with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['YEAR', 'COUNTRY',
                             'Basic Needs', 'SCORE', 'RANK',
                             'Foundations of Wellbeing', 'SCORE', 'RANK',
                             'Opportunity', 'SCORE', 'RANK'])

    # Initialize the Country variable outside the loop
    Country = ''

    # Split text into lines
    entries = text.split('\n')

    # Iterate through each entry on the page
    for i, entry in enumerate(entries, start=1):
        key_values = entry.split()

        if i == 3:
            Country = str(key_values[0])

        phrases_to_find = ["Basic Needs", "Foundations of Wellbeing", "Opportunity"]
        for phrase in phrases_to_find:
            # phrase_match = re.search(phrase + r'\s+(\d+\.\d+)', parsed_text)
            phrase_match = re.search(phrase + r'\s+(\d+\.\d+)\s+(\d+)', text)
            if phrase_match:
                Str_value = phrase_match.group(1)
                Str_Rank = phrase_match.group(2)
                Str_Ind = phrase
                # Country_Name=get_country(pdf_path)
                # print(Str_Ind)
                # print(Str_value)
                # print(Str_Rank)
                # print(Country_Name)
                data.append((year, Country,
                             Str_Ind + '_CODE', Str_value, Str_Rank))

    # Write data to CSV
    with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)  # Write data rows

print('Completed...')
