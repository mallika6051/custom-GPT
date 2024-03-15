# import re
# string="Mallika"
#
# if re.search(string,"I am Mallika Mallika"):
#     print("Match Found")
# else:
#     print("No Match Found")
#
# print(re.findall(string,"I am MallikaMallika"))


# import re
# string = "My domain is python"
# pattern = "python"
# print(re.sub(pattern, "java", string))



# import re
# string = "py.hon"
# pattern = "pydhon"
# if re.match(string,pattern):
#     print("Match found")
# else:
#     print("No match found")




# import re
#
# string = "Hello, world!"
# pattern = "^Hello"
#
# match = re.search(pattern, string)
# if match:
#    print("Match found!")
# else:
#    print("No match found.")





# import re
#
# string ="Hello, World!"
# pattern = "World!$"
#
# match = re.search(pattern, string)
# if match:
#     print("Match found!")
# else:
#     print("No match found.")





# import re
#
# string = "Hello, World!"
# pattern = "[aeiou]"
#
# matches = re.findall(pattern, string)
# print(matches)


# import re
#
# string = "Hellooo, Python!"
# pattern = "o*"
#
# matches = re.findall(pattern, string)
# print(matches)






import re

string = "Mallika Selvam, 21 years old"
pattern = r"(\w+) (\w+), (\d+) years old"

matches = re.findall(pattern, string)
print(matches)
