# import cv2
# import numpy as np
#
# # Load the image
# image = cv2.imread(r'C:\Users\SightSpectrum\PycharmProjects\pythonProject2\Task.jpeg')
#
# # Convert the image to grayscale
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# # Threshold the image to separate black regions
# _, thresholded = cv2.threshold(gray_image, 10, 255, cv2.THRESH_BINARY)
#
# # Invert the thresholded image
# thresholded = cv2.bitwise_not(thresholded)
#
# # Find contours in the thresholded image
# contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
# # Iterate through each contour
# for contour in contours:
#     # Get the bounding box of the contour
#     x, y, w, h = cv2.boundingRect(contour)
#
#     # Create a mask for the current contour
#     mask = np.zeros_like(gray_image)
#     cv2.drawContours(mask, [contour], -1, 255, -1)
#
#     # Inpaint the masked area
#     inpainted_region = cv2.inpaint(image, mask, inpaintRadius=3, flags=cv2.INPAINT_TELEA)
#
#     # Display the inpainted region
#     cv2.imshow('Inpainted Region', inpainted_region)
#     cv2.waitKey(0)
#
# # Close all OpenCV windows
# cv2.destroyAllWindows()




# import cv2
# import numpy as np
# import pytesseract
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# # Load the image
# image = cv2.imread(r'C:\Users\SightSpectrum\PycharmProjects\pythonProject2\Task.jpeg')
#
# # Convert the image to grayscale
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# # Threshold the image to separate black regions
# _, thresholded = cv2.threshold(gray_image, 10, 255, cv2.THRESH_BINARY)
#
# # Invert the thresholded image
# thresholded = cv2.bitwise_not(thresholded)
#
# # Find contours in the thresholded image
# contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
# # Create a mask for the black regions
# black_mask = np.zeros_like(gray_image)
# for contour in contours:
#     cv2.drawContours(black_mask, [contour], -1, 255, -1)
#
# # Invert the black mask
# black_mask = cv2.bitwise_not(black_mask)
#
# # Apply the black mask to the image
# masked_image = cv2.bitwise_and(image, image, mask=black_mask)
#
# # Convert the masked image to grayscale
# gray_masked_image = cv2.cvtColor(masked_image, cv2.COLOR_BGR2GRAY)
#
# # Perform OCR on the gray masked image
# text = pytesseract.image_to_string(gray_masked_image)
#
# # Print the extracted text
# print("Extracted Text:")
# print(text)











# from PIL import Image
# import pytesseract
#
# # Specify the path to the Tesseract executable
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#
# # Open the image
# img = Image.open(r'C:\Users\SightSpectrum\PycharmProjects\pythonProject2\Task\Test.jpeg')
#
# # Convert the image to grayscale
# img = img.convert('L')
#
# # Perform OCR on the image
# text = pytesseract.image_to_string(img)
#
# # Print the extracted text
# print(text)


from PIL import Image
import pytesseract
import cv2

# Specify the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load the image
img = cv2.imread(r'C:\Users\SightSpectrum\PycharmProjects\pythonProject2\Task\Test.jpeg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding to enhance the text
_, threshold = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# Use a kernel to perform morphological operations (optional)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
morphology = cv2.morphologyEx(threshold, cv2.MORPH_CLOSE, kernel)

# Save the preprocessed image for debugging (optional)
cv2.imwrite('preprocessed_image.jpg', morphology)

# Perform OCR on the preprocessed image
text = pytesseract.image_to_string(morphology)

# Print the extracted text
print(text)






# import cv2
# import numpy as np
#
# # Load the image
# image = cv2.imread(r'C:\Users\SightSpectrum\PycharmProjects\pythonProject2\Task.jpeg')
#
# # Convert the image to grayscale
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# # Threshold the image to separate black regions
# _, thresholded = cv2.threshold(gray_image, 10, 255, cv2.THRESH_BINARY)
#
# # Invert the thresholded image
# thresholded = cv2.bitwise_not(thresholded)
#
# # Inpaint the thresholded image to fill in the black regions
# inpainted_region = cv2.inpaint(image, thresholded, inpaintRadius=3, flags=cv2.INPAINT_TELEA)
#
# # Display the inpainted region
# cv2.imshow('Inpainted Region', inpainted_region)
# cv2.waitKey(0)
#
# # Close all OpenCV windows
# cv2.destroyAllWindows()
