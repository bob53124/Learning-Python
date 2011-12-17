# The name of the text file is one of your choice or ex15_sample.txt
from sys import argv
script = argv
filename = raw_input("Enter filename of text file > ")
txt = open(filename)
print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)
print txt_again.read()
