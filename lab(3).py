# a) Create a text file called king.txt in drive C within PyFiles folder.
file_path = "C:\\Users\\user\\Desktop\\PyFiles\\king.txt"

# b) Writes the initial text into king.txt.
initial_text = """A five-day visit to Kenya by Britains King Charles III is unearthing memories of atrocities committed during
the six-decade colonization of the East African country.
"""

with open(file_path, "w") as file:
    file.write(initial_text)

# c) Reads and displays the content of king.txt after writing into the file.
print("Contents of king.txt after writing:")
with open(file_path, "r") as file:
    content = file.read()
    print(content)

#  Appends the text into king.txt.
appended_text = """Charless presence has elicited mixed reactions among Kenyans. Some see it as a reminder of the
dark colonial past, during which thousands of people were tortured and killed as they fought for the
countrys independence. Others say the visit should be viewed as a new chapter in the two countries’
relationship
"""

with open(file_path, "a") as file:
    file.write(appended_text)

# e) Reads and displays the contents of king.txt after appending the text into the file.
print("\nContents of king.txt after appending:")
with open(file_path, "r") as file:
    content = file.read()
    print(content)