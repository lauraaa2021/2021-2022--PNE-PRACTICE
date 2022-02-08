#library someone has written for us to open file , to know where a file is
#in order to import it we will put from and importa or just import and the name

from pathlib import Path

# -- Constant with the new of the file to open
# we create a variable with capital name which is not a constant but kind of
#the filename corresponds to one of the files we have created in the session 4 file
#we want to open RNU gene
FILENAME = "ADA.txt"

#we call one method to open a class file.
#instead of using open filename as we just use the path( filename).read_text() which is going to read directly the file for us without needing to write any other thing
# the way we read it is stored in a variable
# -- Open and read the file
file_contents = Path(FILENAME).read_text()

# -- Print the contents on the console
print(file_contents)