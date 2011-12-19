from sys import argv
from os.path import exists
script = argv
from_file = input("File You Wish To Copy > ")
to_file = input("Where You Would Like To Copy It To > ")

print("Copying form %s to %s" % (from_file, to_file))

# we could do these two on one line too, how?
input = open(from_file)
indata = input.read()

print("The input file is %d bystes long" % len(indata))

print("Does the output file exist? %r" % exists(to_file))
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

output = open(to_file, 'w')
output.write(indata)

print("Alright, all done.")

output.close()
input.close()
