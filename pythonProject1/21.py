# import fitz
# import os
# import cv2
# import numpy as np
#
# def extract_images_from_pdf(pdf_path, output_folder):
#     # Create the output folder if it doesn't exist
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)
#
#     # Open the PDF file
#     doc = fitz.open(pdf_path)
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
#             # Detect and extract yellow-highlighted text
#             extract_yellow_highlighted_text(image_path)
#
#     # Close the PDF file
#     doc.close()
#
# def extract_yellow_highlighted_text(image_path):
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
#     # Iterate through contours
#     for contour in contours:
#         # Get the bounding box of the contour
#         x, y, w, h = cv2.boundingRect(contour)
#
#         # Crop the original image to extract the yellow-highlighted text
#         yellow_highlighted_text = img[y:y+h, x:x+w]
#
#         # Save the extracted yellow-highlighted text as a new image
#         output_image_path = image_path.replace('.', f'_yellow_text_{x}_{y}.')
#         cv2.imwrite(output_image_path, yellow_highlighted_text)
#
#         print(f"Yellow-highlighted text extracted and saved as: {output_image_path}")
#
# if __name__ == "__main__":
#     pdf_path = r'C:\Users\SightSpectrum\PycharmProjects\pythonProject1\Amendment Request Version 92603374temp0.pdf'
#     output_folder = 'output_images'
#     extract_images_from_pdf(pdf_path, output_folder)



import fitz
import os
import cv2
import numpy as np

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
            extract_right_text(image_path)

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
    for contour in contours:
        # Get the bounding box of the contour
        x, y, w, h = cv2.boundingRect(contour)

        # Define the region of interest (ROI) to extract right-side text
        roi_x = x + w
        roi_w = min(img.shape[1] - roi_x, 400)  # Adjust 400 as needed to control the width of the extracted text
        roi = img[y:y+h, roi_x:roi_x + roi_w]

        # Save the extracted right-side text as a new image
        output_image_path = image_path.replace('.', f'_right_text_{x}_{y}.')
        cv2.imwrite(output_image_path, roi)

        print(f"Right-side text extracted and saved as: {output_image_path}")

if __name__ == "__main__":
    pdf_path = r'C:\Users\SightSpectrum\PycharmProjects\pythonProject1\Amendment Request Version 92603374temp0.pdf'
    output_folder = 'output_images'
    extract_images_from_pdf(pdf_path, output_folder)




#
# import fitz
# import os
# import cv2
# import numpy as np
#
# def extract_images_from_pdf(pdf_path, output_folder):
#     # Create the output folder if it doesn't exist
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)
#
#     # Open the PDF file
#     doc = fitz.open(pdf_path)
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
#             # Detect and remove yellow-highlighted right-side text
#             remove_right_highlighted_text(image_path)
#
#     # Close the PDF file
#     doc.close()
#
# def remove_right_highlighted_text(image_path):
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
#     # Remove right-side text adjacent to yellow-highlighted regions
#     for contour in contours:
#         # Get the bounding box of the contour
#         x, y, w, h = cv2.boundingRect(contour)
#
#         # Define the region of interest (ROI) to remove right-side text
#         roi_x = x + w
#         roi_w = min(img.shape[1] - roi_x, 200)  # Adjust the width of the region as needed
#         roi = img[y:y+h, roi_x:roi_x + roi_w]
#
#         # Fill the ROI with white color to remove the text
#         roi[:, :] = (255, 255, 255)  # Fill with white color
#
#     # Save the modified image
#     output_image_path = image_path.replace('.', '_no_right_highlight.')
#     cv2.imwrite(output_image_path, img)
#
#     print(f"Image with yellow-highlighted right-side text removed and saved as: {output_image_path}")
#
# if __name__ == "__main__":
#     pdf_path = r'C:\Users\SightSpectrum\PycharmProjects\pythonProject1\Amendment Request Version 92603374temp0.pdf'
#     output_folder = 'output_images'
#     extract_images_from_pdf(pdf_path, output_folder)
#



# import fitz
# import os
# import cv2
# import numpy as np
#
# def extract_images_from_pdf(pdf_path, output_folder):
#     # Create the output folder if it doesn't exist
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)
#
#     # Open the PDF file
#     doc = fitz.open(pdf_path)
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
#             # Remove yellow-highlighted regions and right-side lines
#             remove_yellow_highlighted(image_path)
#
#     # Close the PDF file
#     doc.close()
#
# def remove_yellow_highlighted(image_path):
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
#     # Remove yellow-highlighted regions
#     img_no_yellow = cv2.bitwise_and(img, img, mask=cv2.bitwise_not(yellow_mask))
#
#     # Find contours in the yellow mask
#     contours, _ = cv2.findContours(yellow_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
#     # Remove right-side lines adjacent to yellow-highlighted regions
#     for contour in contours:
#         # Get the bounding box of the contour
#         x, y, w, h = cv2.boundingRect(contour)
#
#         # Define the region of interest (ROI) to remove right-side lines
#         roi_x = x + w
#         roi_w = min(img.shape[1] - roi_x, 200)  # Adjust the width of the region as needed
#         roi = img_no_yellow[y:y+h, roi_x:roi_x + roi_w]
#
#         # Fill the ROI with white color to remove the right-side lines
#         roi[:, :] = (255, 255, 255)  # Fill with white color
#
#     # Save the modified image
#     output_image_path = image_path.replace('.', '_no_yellow_highlight.')
#     cv2.imwrite(output_image_path, img_no_yellow)
#
#     print(f"Image with yellow-highlighted regions and right-side lines removed and saved as: {output_image_path}")
#
# if __name__ == "__main__":
#     pdf_path = r'C:\Users\SightSpectrum\PycharmProjects\pythonProject1\Amendment Request Version 92603374temp0.pdf'
#     output_folder = 'output_images'
#     extract_images_from_pdf(pdf_path, output_folder)
