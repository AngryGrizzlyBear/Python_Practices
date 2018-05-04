# These are variables!
people = 40
cars = 40
buses = 40

# If cars are greater than people, print this sentence.
if cars > people:
    print "We should take the cars."
# Else, If cars are less than people, print this sentence.
elif cars < people:
    print "We should not take the cars."
# Otherwise, print this if it doesn't meet the first two criteria. 
else:
    print "We can't decide."
# Same as stated above. 
if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we can take the buses."
else:
    print "We still can't decide."

if people > buses:
    print "Alright, let's just take busses."
else:
    print "Fine, let's just stay home then."


