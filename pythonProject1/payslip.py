# import PyPDF2
#
# # Open the PDF file in binary mode
# with open(r'C:\Users\SightSpectrum\PycharmProjects\pythonProject1/Example.pdf', 'rb') as file:
#     # Create a PDF reader object
#     pdf_reader = PyPDF2.PdfReader(file)
#
#     # Get the number of pages in the PDF
#     num_pages = len(pdf_reader.pages)
#
#     # Extract text from each page
#     for page_number in range(num_pages):
#         page = pdf_reader.pages[page_number]
#         text = page.extract_text()
#     print(text)
#
#         # Do further processing on the extracted text
#         # For example, you can search for marked data or patterns in the text
#         # and extract the relevant information





# import fitz  # PyMuPDF
#
# # Open the PDF file
# # pdf_file = r'C:\Users\SightSpectrum\PycharmProjects\pythonProject1\Example.pdf'
# pdf_file = r'C:\Users\SightSpectrum\PycharmProjects\pythonProject1\Amendment Request Version 92603374temp0.pdf'
# pdf_document = fitz.open(pdf_file)
#
# highlighted_text = []
#
# # Iterate through each page in the PDF
# for page_number in range(len(pdf_document)):
#     page = pdf_document.load_page(page_number)
#
#     # Get the annotations on the page
#     annotations = page.annots()
#
#     # Iterate through annotations
#     for annot in annotations:
#         # Check if the annotation subtype is 'Highlight'
#         if annot.type[0] == 8:  # 8 corresponds to 'Highlight' annotation type
#             # Get the quad points of the annotation
#             quad_points = annot.vertices
#
#             # Flatten the quad points and extract the coordinates of two opposite corners
#             x_values = [quad_points[i][0] for i in range(len(quad_points))]
#             y_values = [quad_points[i][1] for i in range(len(quad_points))]
#             x0, x1 = min(x_values), max(x_values)
#             y0, y1 = min(y_values), max(y_values)
#
#             # Create a fitz.Rect object
#             rect = fitz.Rect(x0, y0, x1, y1)
#
#             # Extract the text within the bounding rectangle of the quad points
#             words = page.get_text("words", clip=rect)
#
#             # Append the extracted text to the list
#             highlighted_text.append(' '.join(word[4] for word in words))
#
# # Print the highlighted text
# print(highlighted_text)
#
# # Close the PDF document
# pdf_document.close()



import fitz  # PyMuPDF

# Open the PDF file
pdf_file = r'C:\Users\SightSpectrum\PycharmProjects\pythonProject1\Example.pdf'
pdf_document = fitz.open(pdf_file)

highlighted_text = []

# Iterate through each page in the PDF
for page_number in range(len(pdf_document)):
    page = pdf_document.load_page(page_number)

    # Get the annotations on the page and convert them to a list
    annotations = list(page.annots())

    print(f"Page {page_number + 1} - Number of Annotations: {len(annotations)}")

    # Iterate through annotations
    for annot in annotations:
        try:
            # Check if the annotation subtype is 'Highlight'
            if annot.type[0] == 8:  # 8 corresponds to 'Highlight' annotation type
                # Extract the quad points of the annotation
                quad_points = annot.vertices

                print(f"Quad Points: {quad_points}")

                # Ensure quad points contain numeric values
                if all(isinstance(coord, (int, float)) for coord in quad_points):
                    # Extract the x and y coordinates
                    x_values = quad_points[0::2]
                    y_values = quad_points[1::2]

                    # Create a fitz.Rect object from the extracted coordinates
                    rect = fitz.Rect(min(x_values), min(y_values), max(x_values), max(y_values))

                    # Extract the text within the bounding rectangle of the quad points
                    words = page.get_text("words", clip=rect)

                    # Append the extracted text to the list
                    highlighted_text.append(' '.join(word[4] for word in words))
        except Exception as e:
            print(f"Error processing annotation: {e}")

# Print the highlighted text
print("\nHighlighted Text:")
for text in highlighted_text:
    print(text)

# Close the PDF document
pdf_document.close()







# import fitz  # PyMuPDF
#
# # Open the PDF file
# pdf_file = r'C:\Users\SightSpectrum\PycharmProjects\pythonProject1\Example.pdf'
# pdf_document = fitz.open(pdf_file)
#
# highlighted_text = []
#
# # Iterate through each page in the PDF
# for page_number in range(len(pdf_document)):
#     page = pdf_document.load_page(page_number)
#
#     # Get the annotations on the page
#     annotations = page.annots()
#
#     # Iterate through annotations
#     for annot in annotations:
#         # Check if the annotation subtype is 'Highlight'
#         if annot.type[0] == 8:  # 8 corresponds to 'Highlight' annotation type
#             # Get the quad points of the annotation
#             quad_points = annot.vertices
#
#             # Flatten the quad points and extract the coordinates of two opposite corners
#             x_values = [quad_points[i][0] for i in range(len(quad_points))]
#             y_values = [quad_points[i][1] for i in range(len(quad_points))]
#             x0, x1 = min(x_values), max(x_values)
#             y0, y1 = min(y_values), max(y_values)
#
#             # Create a fitz.Rect object
#             rect = fitz.Rect(x0, y0, x1, y1)
#
#             # Extract the text within the bounding rectangle of the quad points
#             words = page.get_text("words", clip=rect)
#
#             # Replace the extracted text with "mallika"
#             modified_words = []
#             for word in words:
#                 modified_word = list(word)
#                 modified_word[4] = "mallika"
#                 modified_words.append(modified_word)
#
#             # Append the modified text to the list
#             highlighted_text.append(' '.join(word[4] for word in modified_words))
#
# # Print the highlighted text with replaced words
# print(highlighted_text)
#
# # Close the PDF document
# pdf_document.close()






#
# import fitz  # PyMuPDF
#
# # Open the original PDF file
# pdf_file = r'C:\Users\SightSpectrum\PycharmProjects\pythonProject1\Example.pdf'
# pdf_document = fitz.open(pdf_file)
#
# # Create a new PDF document
# new_pdf_document = fitz.open()
#
# # Iterate through each page in the original PDF
# for page_number in range(len(pdf_document)):
#     # Load the page from the original PDF document
#     page = pdf_document.load_page(page_number)
#
#     # Create a new page in the new PDF document
#     new_page = new_pdf_document.new_page(width = page.rect.width, height = page.rect.height)
#
#     # Get the annotations on the page
#     annotations = page.annots()
#
#     # Iterate through annotations
#     for annot in annotations:
#         # Check if the annotation subtype is 'Highlight'
#         if annot.type[0] == 8:  # 8 corresponds to 'Highlight' annotation type
#             # Get the quad points of the annotation
#             quad_points = annot.vertices
#
#             # Flatten the quad points and extract the coordinates of two opposite corners
#             x_values = [quad_points[i][0] for i in range(len(quad_points))]
#             y_values = [quad_points[i][1] for i in range(len(quad_points))]
#             x0, x1 = min(x_values), max(x_values)
#             y0, y1 = min(y_values), max(y_values)
#
#             # Create a fitz.Rect object
#             rect = fitz.Rect(x0, y0, x1, y1)
#
#             # Extract the text within the bounding rectangle of the quad points
#             words = page.get_text("words", clip=rect)
#
#             # Replace the extracted text with "mallika"
#             modified_words = []
#             for word in words:
#                 modified_word = list(word)
#                 modified_word[4] = "mallika"
#                 modified_words.append(modified_word)
#
#             # Draw the modified text on the new page
#             new_page.insert_text((x0, y0), ' '.join(word[4] for word in modified_words))
#
# # Save the new PDF document
# new_pdf_document.save(r'C:\Users\SightSpectrum\PycharmProjects\pythonProject1\Modified_PDF.pdf')
#
# # Close the PDF documents
# pdf_document.close()
# new_pdf_document.close()






# import fitz  # PyMuPDF
#
# # Open the original PDF file
# pdf_file = r'C:\Users\SightSpectrum\PycharmProjects\pythonProject1\Example.pdf'
# pdf_document = fitz.open(pdf_file)
#
# # Create a new PDF document
# new_pdf_document = fitz.open()
#
# # Iterate through each page in the original PDF
# for page_number in range(len(pdf_document)):
#     # Load the page from the original PDF document
#     page = pdf_document.load_page(page_number)
#
#     # Create a new page in the new PDF document
#     new_page = new_pdf_document.new_page(width=page.rect.width, height=page.rect.height)
#
#     # Get the text on the page
#     text = page.get_text()
#
#     # Replace the highlighted words with "mallika" in the text
#     for annot in page.annots():
#         if annot.type[0] == 8:  # 8 corresponds to 'Highlight' annotation type
#             quad_points = annot.vertices
#             x_values = [quad_points[i][0] for i in range(len(quad_points))]
#             y_values = [quad_points[i][1] for i in range(len(quad_points))]
#             x0, x1 = min(x_values), max(x_values)
#             y0, y1 = min(y_values), max(y_values)
#             rect = fitz.Rect(x0, y0, x1, y1)
#             highlighted_text = page.get_text("text", clip=rect)
#             text = text.replace(highlighted_text, "mallika")
#
#     # Draw the modified text on the new page
#     new_page.insert_text((0, 0), text)
#
# # Save the new PDF document
# new_pdf_document.save(r'C:\Users\SightSpectrum\PycharmProjects\pythonProject1\Modified_PDF.pdf')
#
# # Close the PDF documents
# pdf_document.close()
# new_pdf_document.close()



# import fitz  # PyMuPDF
#
# def extract_red_marked_words(pdf_file_path):
#     red_marked_words = []
#
#     # Open the PDF file
#     pdf_document = fitz.open(pdf_file_path)
#
#     # Iterate through each page in the PDF
#     for page_number in range(len(pdf_document)):
#         page = pdf_document.load_page(page_number)
#         # Get all text instances on the page
#         text_instances = page.search_for('')
#         if text_instances is None:
#             print(f"No text found on page {page_number + 1}")
#             continue
#         for inst in text_instances:
#             # Get the text object's color
#             color = page.get_text_color(inst)
#             # Check if the text color is red
#             if color == (1.0, 0.0, 0.0):
#                 # Extract the text
#                 marked_text = page.get_text("text", clip=inst)
#                 red_marked_words.append(marked_text.strip())
#
#     # Close the PDF document
#     pdf_document.close()
#
#     return red_marked_words
#
# if __name__ == "__main__":
#     # Define the path to your PDF file
#     pdf_file_path = r'C:\Users\SightSpectrum\PycharmProjects\pythonProject1\Example.pdf'
#
#     # Extract the red-marked words from the PDF
#     red_marked_words = extract_red_marked_words(pdf_file_path)
#
#     # Check if marked words were found
#     if red_marked_words:
#         # Print the marked words
#         print("Red marked words found in the PDF:")
#         for idx, word in enumerate(red_marked_words, 1):
#             print(f"{idx}. {word}")
#     else:
#         print("No red marked words found in the PDF.")
#





# from pypdf import PdfReader
# reader = PdfReader(r'C:\Users\SightSpectrum\PycharmProjects\pythonProject1\Example.pdf')
# print(len(reader.pages))
# page = reader.pages[0]
# print(page.extract_text())



# import fitz
# doc = fitz.open(r'C:\Users\SightSpectrum\PycharmProjects\pythonProject1\Example.pdf')
# print(doc.page_count)
# print(doc.metadata)
