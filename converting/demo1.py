# import fitz
# doc = fitz.open('ARE.pdf')
# text = ""
# for page in doc:
#     text+=page.get_text()
# print(text)


import fitz

def add_index_to_words(text):
    words = text.split()
    result = []
    for i, word in enumerate(words, start=1):
        result.append(f"{i} {word}")
    return ' '.join(result)

doc = fitz.open('ARE.pdf')
for i, page in enumerate(doc):
    text = page.get_text()
    modified_text = add_index_to_words(text)
    print(f"Page {i + 1}:\n{modified_text}\n{'=' * 20}")










