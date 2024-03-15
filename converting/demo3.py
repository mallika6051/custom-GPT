# import PyPDF2
#
# def print_text_from_pdf(input_pdf, text_to_remove):
#     with open(input_pdf, 'rb') as file:
#         pdf_reader = PyPDF2.PdfReader(file)
#
#         for page_number in range(len(pdf_reader.pages)):
#             page = pdf_reader.pages[page_number]
#             text = page.extract_text()
#
#             # Split text into lines and print each line with its index
#             lines = text.split('\n')
#             for line_index, line_content in enumerate(lines):
#                 if text_to_remove not in line_content:
#                     print(f"Line {line_index}:\n{line_content}")
#
# # Example usage9
# input_pdf_file = 'ARE.pdf'
# text_to_remove = 'Text you want to remove'
#
# print_text_from_pdf(input_pdf_file, text_to_remove)






# import PyPDF2
#
# def print_text_from_pdf(input_pdf, lines_to_remove):
#     with open(input_pdf, 'rb') as file:
#         pdf_reader = PyPDF2.PdfReader(file)
#
#         for page_number in range(len(pdf_reader.pages)):
#             page = pdf_reader.pages[page_number]
#             text = page.extract_text()
#
#             # Split text into lines
#             lines = text.split('\n')
#
#             # Print each line excluding specified lines
#             for line_index, line_content in enumerate(lines):
#                 if line_index not in lines_to_remove:
#                     print(f"Line {line_index}:\n{line_content}")
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
# print_text_from_pdf(input_pdf_file, lines_to_remove)












import PyPDF2

def print_text_from_pdf(input_pdf, lines_to_remove):
    with open(input_pdf, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)

        # Initialize a flag to identify whether to print column names
        print_columns = False

        for page_number in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_number]
            text = page.extract_text()

            # Split text into lines
            lines = text.split('\n')

            # Process lines separately for column names (lines 9 to 17)
            for line_index, line_content in enumerate(lines):
                if line_index in [9, 10, 11, 12, 13, 14, 15, 16, 17]:
                    print_columns = True
                    print(f"Column Name Line {line_index}:\n{line_content}")
                elif line_index not in lines_to_remove:
                    if print_columns:
                        # Print column names in tabular format
                        print('\t'.join(lines[9:18]))
                        print_columns = False
                    # print(f"Line {line_index}:\n{line_content}")

# Example usage
input_pdf_file = 'ARE.pdf'

# Get the total number of lines in the document
with open(input_pdf_file, 'rb') as file:
    pdf_reader = PyPDF2.PdfReader(file)
    total_lines = sum(len(page.extract_text().split('\n')) for page in pdf_reader.pages)

# Define the lines to remove (from index 0 to 7 and from 239 to the end)
lines_to_remove = list(range(8)) + list(range(239, total_lines))

print_text_from_pdf(input_pdf_file, lines_to_remove)






















#
# import PyPDF2
# import csv
#
# def extract_columns_from_pdf(input_pdf, lines_to_remove):
#     extracted_lines = []
#
#     with open(input_pdf, 'rb') as file:
#         pdf_reader = PyPDF2.PdfReader(file)
#
#         # Initialize a flag to identify whether to print column names
#         print_columns = False
#
#         for page_number in range(len(pdf_reader.pages)):
#             page = pdf_reader.pages[page_number]
#             text = page.extract_text()
#
#             # Split text into lines
#             lines = text.split('\n')
#
#             # Process lines separately for column names (lines 9 to 17)
#             for line_index, line_content in enumerate(lines):
#                 if line_index in [9, 10, 11, 12, 13, 14, 15, 16, 17]:
#                     print_columns = True
#                     # Store the column name lines in a list
#                     extracted_lines.append([f"Column Name Line {line_index}:", line_content])
#                 elif line_index not in lines_to_remove:
#                     if print_columns:
#                         # Store the column names in tabular format
#                         extracted_lines.append(lines[9:18])
#                         print_columns = False
#
#     return extracted_lines
#
# def write_to_csv(output_csv, extracted_lines):
#     with open(output_csv, 'w', newline='', encoding='utf-8') as csv_file:
#         csv_writer = csv.writer(csv_file)
#         csv_writer.writerows(extracted_lines)
#
# # Example usage
# input_pdf_file = 'ARE.pdf'
# output_csv_file = 'Final.csv'
#
# # Get the total number of lines in the document
# with open(input_pdf_file, 'rb') as file:
#     pdf_reader = PyPDF2.PdfReader(file)
#     total_lines = sum(len(page.extract_text().split('\n')) for page in pdf_reader.pages)
#
# # Define the lines to remove (from index 0 to 7 and from 239 to the end)
# lines_to_remove = list(range(8)) + list(range(239, total_lines))
#
# # Extract lines and write to CSV
# extracted_lines = extract_columns_from_pdf(input_pdf_file, lines_to_remove)
# write_to_csv(output_csv_file, extracted_lines)
#
