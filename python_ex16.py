# Importing argv from sys
from sys import argv
# Defining Variables.
script, filename = argv
# Making a string that's letting people know that we're going to erase %r, which is assigned to filename. Which will be called when we call it through python.
print "We're going to erase %r." % filename
# Printing to have the user imput a command. 
print "If you don't want that, hit CTRL-C (^C)."
# Same as comment above. 
print "If you do want that, hit RETURN."
# Pick your choice. 
raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write("%s \n %s \n %s" % (line1, line2, line3) )
# target.write(line1)
# target.write("\n")
#target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

print "And finally, we close it."
target.close()