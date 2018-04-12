from sys import argv

script, first, second, third = argv

question = raw_input("Do you know what this is? ")
fourth = raw_input("What is your fourth? ")
fifth = raw_input("What is your fifth? ")
sixth = raw_input("What is your sixth? ") 
print "Ah....%r" % question
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

print("for your script %r, these are the variables: %r, %r, %r, %r, %r, and %r") %(script, first, second, third, fourth, fifth, sixth)


# If you don't print out 3 after running the script, you'll receive an error. Python will find the script, due to script? 
# However, first, second, third must be called in the terminal to run. We have three variables, so we must be able to 
# define those three before moving along.

# The Difference between argv and raw_input() is that the user is required to give an input with raw_input(). 
# If you give someone a script input on the command line, then you use argv. 
# If you want them to input using the keyboard while the script is running, then use raw_input()
