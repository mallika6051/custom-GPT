# output in text format

import fitz
import os
import cv2
import numpy as np
import pytesseract

def extract_images_from_pdf(pdf_path, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the PDF file
    doc = fitz.open(pdf_path)

    # Iterate through each page
    for page_number in range(len(doc)):
        page = doc.load_page(page_number)

        # Get the image list for the current page
        image_list = page.get_images(full=True)

        # Iterate through each image on the page
        for image_index, img in enumerate(image_list):
            xref = img[0]
            base_image = doc.extract_image(xref)

            # Get the image data
            image_data = base_image["image"]

            # Determine the image type (extension)
            image_ext = base_image["ext"]

            # Save the image to the output folder
            image_path = os.path.join(output_folder, f"page_{page_number}_image_{image_index}.{image_ext}")
            with open(image_path, "wb") as image_file:
                image_file.write(image_data)

            # Detect and extract lines of text to the right of yellow-highlighted regions
            extracted_text = extract_right_text(image_path)
            print("Extracted text:", extracted_text)

    # Close the PDF file
    doc.close()

def extract_right_text(image_path):
    # Load the image
    img = cv2.imread(image_path)

    # Convert the image to HSV color space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define the lower and upper bounds for the yellow color in HSV
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])

    # Threshold the HSV image to get a mask containing only the yellow regions
    yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # Find contours in the yellow mask
    contours, _ = cv2.findContours(yellow_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Extract right-side text lines adjacent to yellow-highlighted regions
    extracted_text = []

    for contour in contours:
        # Get the bounding box of the contour
        x, y, w, h = cv2.boundingRect(contour)

        # Define the region of interest (ROI) to extract right-side text
        roi_x = x + w
        roi_w = min(img.shape[1] - roi_x, 400)  # Adjust 400 as needed to control the width of the extracted text
        roi = img[y:y+h, roi_x:roi_x + roi_w]

        # Perform OCR on the region of interest
        text = pytesseract.image_to_string(roi)
        extracted_text.append(text.strip())

    return extracted_text

if __name__ == "__main__":
    pdf_path = r'C:\Users\SightSpectrum\PycharmProjects\pythonProject1\Amendment Request Version 92603374temp0.pdf'
    output_folder = 'output_images'
    extract_images_from_pdf(pdf_path, output_folder)



# perfect output in csv



# import fitz
# import os
# import cv2
# import numpy as np
# import pytesseract
# import csv
#
# def extract_images_from_pdf(pdf_path, output_folder):
#     # Create the output folder if it doesn't exist
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)
#
#     # Open the PDF file
#     doc = fitz.open(pdf_path)
#
#     # Create a list to hold all extracted words
#     all_extracted_words = []
#
#     # Iterate through each page
#     for page_number in range(len(doc)):
#         page = doc.load_page(page_number)
#
#         # Get the image list for the current page
#         image_list = page.get_images(full=True)
#
#         # Iterate through each image on the page
#         for image_index, img in enumerate(image_list):
#             xref = img[0]
#             base_image = doc.extract_image(xref)
#
#             # Get the image data
#             image_data = base_image["image"]
#
#             # Determine the image type (extension)
#             image_ext = base_image["ext"]
#
#             # Save the image to the output folder
#             image_path = os.path.join(output_folder, f"page_{page_number}_image_{image_index}.{image_ext}")
#             with open(image_path, "wb") as image_file:
#                 image_file.write(image_data)
#
#             # Detect and extract words to the right of yellow-highlighted regions
#             extracted_words = extract_right_words(image_path)
#
#             # Add extracted words to the list
#             all_extracted_words.extend(extracted_words)
#
#     # Write all extracted words to a CSV file
#     csv_file_path = os.path.join(output_folder, 'extracted_words.csv')
#     with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
#         csv_writer = csv.writer(csv_file)
#         csv_writer.writerow(['Extracted Words'])
#         for word in all_extracted_words:
#             csv_writer.writerow([word])
#
#     # Close the PDF file
#     doc.close()
#
# def extract_right_words(image_path):
#     # Load the image
#     img = cv2.imread(image_path)
#
#     # Convert the image to HSV color space
#     hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#
#     # Define the lower and upper bounds for the yellow color in HSV
#     lower_yellow = np.array([20, 100, 100])
#     upper_yellow = np.array([30, 255, 255])
#
#     # Threshold the HSV image to get a mask containing only the yellow regions
#     yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
#
#     # Find contours in the yellow mask
#     contours, _ = cv2.findContours(yellow_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
#     # Extract right-side words adjacent to yellow-highlighted regions
#     extracted_words = []
#
#     for contour in contours:
#         # Get the bounding box of the contour
#         x, y, w, h = cv2.boundingRect(contour)
#
#         # Define the region of interest (ROI) to extract right-side text
#         roi_x = x + w
#         roi_w = min(img.shape[1] - roi_x, 400)  # Adjust 400 as needed to control the width of the extracted text
#         roi = img[y:y+h, roi_x:roi_x + roi_w]
#
#         # Perform OCR on the region of interest
#         text = pytesseract.image_to_string(roi)
#
#         # Split the text into individual words
#         words = text.split()
#
#         # Append each word to the extracted_words list
#         extracted_words.extend(words)
#
#     return extracted_words
#
#
# if __name__ == "__main__":
#     pdf_path = r'C:\Users\SightSpectrum\PycharmProjects\pythonProject1\Amendment Request Version 92603374temp0.pdf'
#     output_folder = 'output_images'
#     extract_images_from_pdf(pdf_path, output_folder)
