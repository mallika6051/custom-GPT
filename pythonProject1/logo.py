# import fitz  # PyMuPDF
#
# def extract_bold_right_text(pdf_path):
#     bold_right_text = []
#
#     # Open the PDF file
#     doc = fitz.open(pdf_path)
#
#     # Iterate through each page
#     for page_number in range(len(doc)):
#         page = doc.load_page(page_number)
#
#         # Extract text from the page
#         page_text = page.get_text()
#
#         # Get the blocks of text along with font attributes
#         blocks = page.get_text("dict")["blocks"]
#
#         print(f"Page {page_number + 1} Blocks: {blocks}")
#
#         for b in blocks:
#             if "lines" in b:  # Check if the key 'lines' exists
#                 for l in b["lines"]:
#                     for s in l["spans"]:
#                         # Check if the text is bold and aligned to the right
#                         if s["flags"] & 2 and s["flags"] & 8:
#                             bold_right_text.append(s["text"])
#
#     # Close the PDF file
#     doc.close()
#
#     return bold_right_text
#
# if __name__ == "__main__":
#     pdf_path = r'C:\Users\SightSpectrum\PycharmProjects\pythonProject1\Amendment Request Version 92603374temp0.pdf'
#     extracted_text = extract_bold_right_text(pdf_path)
#     for text in extracted_text:
#         print(text)



# class mallika:
#     def fun1(self, name, age):
#         self.name = name
#         self.age = age
# obj=mallika()
# obj.fun1('mallika',21)
# print(obj.name ,
# obj.age )


# class Example:
#     def __init__(self):
#         # Public attribute
#         self.public_var = "Public Variable"
#
#         # Protected attribute (by convention)
#         self._protected_var = "Protected Variable"
#
#         # Private attribute (by convention)
#         self.__private_var = "Private Variable"
#
#     def public_method(self):
#         print("This is a public method")
#
#     def _protected_method(self):
#         print("This is a protected method")
#
#     def __private_method(self):
#         print("This is a private method")
#
# # Create an instance of the class
# obj = Example()
#
# # Accessing public attributes and methods
# print(obj.public_var)    # Output: Public Variable
# obj.public_method()      # Output: This is a public method
#
# print(obj._protected_var)    # Output: Protected Variable
# obj._protected_method()      # Output: This is a protected method
#
# print(obj._Example__private_var)    # Output: Private Variable
# obj._Example__private_method()




# class A :
#     def fun1(self):
#         print("Hello")
# class B(A):
#     def fun1(self):
#         print("Mallika")
# obj=B()
# obj.fun1()


# from abc import ABC, abstractmethod
#
# class A(ABC):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     @abstractmethod
#     def hai(self):
#         print("Hai")
# class B(A):
#     def hai(self):
#         print(self.name)
# obj=B("Mallika", 21)
# obj.hai()

# class A:
#     a="public"
#     _b="protected"
#     __c="private"
#     def public(self):
#         print("hai")
#     def _protected(self):
#         print("hello")
#     def __private(self):
#         print("welcome")
# class B(A):
#     def hai(self):
#         print("hello")
# obj=B()
# print(obj.a)
# obj.public()
#
# print(obj._b)
# obj._protected()
# print(obj._A__c)
# obj._A__private()

