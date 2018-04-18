# This is importing argv from system.
from sys import argv
# this assigning the script and input file to argv
script, input_file = argv
# Creates a function 'rpint_all(f)' which reads and prints the input
def print_all(f):
    print f.read()

# Creates a function 'rewind(f)' which sets the input files current position 
# to 0 via the 'seek()' function.
def rewind(f):
    f.seek(0)
# This is going to count each line in the called script
def print_a_line(line_count, f):
    print line_count, f.readline()
# This is calling the input_file that's going to be open.
current_file = open(input_file)

print "First let's print the whole file:\n"
# This is more than likely opening up current file, which stated above is open(input_file), which is = argv.
print_all(current_file)

print "Now let's rewind, kind of like a tape.\n"
# This resets the file for reprinting.
rewind(current_file)

print "Let's print three lines:\n"
# This now prints this topic on three lines. Changed the operand to += 1, which basically says += 1 is the same as saying current_line = current_line + 1
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
