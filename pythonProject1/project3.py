# import fitz  # PyMuPDF
# from PIL import Image
# import io
# import os
#
# def extract_images_from_pdf(pdf_path, output_folder):
#     doc = fitz.open(pdf_path)
#
#     # Create the output folder if it doesn't exist
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)
#
#     for page_number in range(len(doc)):
#         page = doc.load_page(page_number)
#         image_list = page.get_images(full=True)
#
#         for image_index, img in enumerate(image_list):
#             xref = img[0]
#             base_image = doc.extract_image(xref)
#             image_bytes = base_image["image"]
#             image = Image.open(io.BytesIO(image_bytes))
#
#             image_path = os.path.join(output_folder, f"page_{page_number}_image_{image_index}.png")
#             image.save(image_path)
#
#     doc.close()
#
# if __name__ == "__main__":
#     pdf_path = r'C:\Users\SightSpectrum\PycharmProjects\pythonProject1\Amendment Request Version 92603374temp0.pdf'
#     output_folder = 'output_images'
#     extract_images_from_pdf(pdf_path, output_folder)








import fitz  # PyMuPDF
import os

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

    # Close the PDF file
    doc.close()

if __name__ == "__main__":
    pdf_path = r'C:\Users\SightSpectrum\PycharmProjects\pythonProject1\Amendment Request Version 92603374temp0.pdf'
    output_folder = 'output_images'
    extract_images_from_pdf(pdf_path, output_folder)
