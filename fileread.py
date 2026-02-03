# file operations - file io

# function 1 : read the file
def read_file():
  file = open("notes.txt","r")
  content = file.read()
  file.close()
  return content

# function 2: write to the file
def write_to_file(text):
  file = open("notes.txt","a")
  file.write(text)
  file.close()

# function 3: to display content

def show_content(content):
  print("----File Content-----")
  print(content)
  print("--------------")

# read and show the original content
print("Step 1: Reading the file")
original = read_file()
show_content(original)

# add new text
print("Step 2 : Add new Text")
write_to_file("Data engineering is all about running the show....\n")
write_to_file("Yipeeeee...")

# read and show the updated content
updated = read_file()
show_content(updated)

print("Done .....Check your notes.txt")