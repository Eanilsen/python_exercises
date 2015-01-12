# Imports the 'argument variable' from the sys package
from sys import argv

# Assigns or "unpacks" the content of 'argv' to variables
script, filename = argv

# Returns a file object and assigns it to the txt variable
txt = open(filename)

# Prints out the name of the file passed to the filename variable
print "Here is your file %r:" % filename
# Prints out the contents of the txt variable
print txt.read()
txt.close()

# Prints a simple string
print "Type the filename again:"
# Stores user input in file_again
file_again = raw_input("> ")

# Creates a file object of the file passed to file_again by the user
txt_again = open(file_again)

# Prints out the contents of txt_again
print txt_again.read()

txt_again.close()
