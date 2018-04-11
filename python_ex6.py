# This is a variable that equals a string.
x = "There are %d types of people." % 10
# this is a variable that equals a string, as well.
binary = "binary"
# this is also a variable that equals a string. These variables can be called later.
do_not = "don't"
# Same with the previous three.
y = "Those who know %s and those who %s." % (binary, do_not)
# this prints variable x
print x
# this prints variable y.
print y
# this prints a variable inside of a string. 
print "I said: %r." % x 
# this also prints a variable inside of a string.
print "I also said: '%s'." % y
# This is a true false statement. I believe we will be going over these in later chapters.
hilarious = False
# This is a variable that prints a string, regardless. Though, I'm not sure why it's able to know that we're talking about hilarious. It's the only one caled by %r, and it also happens to be referencing the variable before hand.
joke_evaluation = "Isn't that joke so funny?! %r"
# Oh, I see it now. It's defined already. Joke Evaluation is calling % hilarious with %r. Nice.
print joke_evaluation % hilarious
# This is a variable.
w = "This is the left side of..."
# This is also a variable.
e = "a string with a right side."
# This will combine two variables. w + e. That's why it'll make it longer. Why? I believe because they're both strings, and adding the two together will make one string. 
print w + e