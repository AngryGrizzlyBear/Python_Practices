# This is importing the module from sys. Read this as, import argv from sys. 
from sys import argv
# We're assigning variables here. script and filename will = argv. When we run the app, I believe it'll be defined. 
# Example would be, python python_ex15.py "Name." 
# Script is defined already, it's the name of the program. 
# However, filename is defined when we run the script.
script, filename = argv
# Might get a little confusing here; however, txt is a variable. 
# We're assigning it to open(filename.) 
# When we call txt, we're having it open the filename. 
# I'll explain more later.
txt = open(filename)
# We're just printing out filename. %r is for debugging purposes. We're going to assign %r to filename.
print "Here's your file %r:" % filename
# Here's the fun part. We're printing txt to read the empty argument. 
# We're calling txt. By calling txt, we're having it read open(filename.) 
# It's kinda' hard to explain, but, we're calling the function to read what we had it open.
print txt.read()

# print "Type the filename again:"
# file_again = raw_input("<> ")

# txt_again = open(file_again)

# print txt_again.read()
print "Type the filename one more time, please:"
file_test = raw_input("> ")
txt_test = open(file_test)
print txt_test.read()

# Using txt = open filename is faster, because raw_input requires for you to input the filename,
#  when you're already entering the filename at the start of the script for the first method. 
# BUT, I will say, that both have their strengths and weaknesses.

txt.close()
# txt_again.close()
txt_test.close()