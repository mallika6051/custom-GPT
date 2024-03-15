# import fitz  # PyMuPDF
#
# def extract_pdf_data(pdf_path):
#     pdf_document = fitz.open(pdf_path)
#
#     for page_num in range(pdf_document.page_count):
#         page = pdf_document[page_num]
#         text_lines = page.get_text("text").split('\n')
#
#         # Skip lines 2 to 8 (index 1 to 7)
#         cleaned_lines = [line for index, line in enumerate(text_lines) if index < 1 or index > 8]
#
#         cleaned_text = '\n'.join(cleaned_lines)
#         print(cleaned_text)
#
# # Replace 'your_file.pdf' with the actual PDF file path
# extract_pdf_data('ARE.pdf')





# import fitz  # PyMuPDF
#
# def extract_and_remove_lines(pdf_path, lines_to_remove=69):
#     pdf_document = fitz.open(pdf_path)
#
#     for page_num in range(pdf_document.page_count):
#         page = pdf_document[page_num]
#         text_lines = page.get_text("text").split('\n')
#
#         # Skip lines 2 to 8 (index 1 to 7)
#         cleaned_lines = [line for index, line in enumerate(text_lines) if index < 1 or index > 8]
#
#         # Remove the last lines
#         cleaned_lines = cleaned_lines[:-lines_to_remove]
#
#         cleaned_text = '\n'.join(cleaned_lines)
#         print(cleaned_text)
#
# # Replace 'your_file.pdf' with the actual PDF file path
# extract_and_remove_lines('ARE.pdf', lines_to_remove=69)





import fitz  # PyMuPDF

def extract_and_remove_lines(pdf_path, lines_to_skip_top=8, lines_to_skip_bottom=69):
    pdf_document = fitz.open(pdf_path)

    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        text_lines = page.get_text("text").split('\n')

        # Skip lines at the top (default is 8)
        cleaned_lines = text_lines[lines_to_skip_top:]

        # Remove lines from the bottom (default is 68)
        cleaned_lines = cleaned_lines[:-lines_to_skip_bottom]

        cleaned_text = '\n'.join(cleaned_lines)
        print(cleaned_text)

# Replace 'your_file.pdf' with the actual PDF file path
extract_and_remove_lines('ARE.pdf')





