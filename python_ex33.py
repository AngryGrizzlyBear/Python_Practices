i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
    print num

def while_loop(limit, increment):
    i = 0
    numbers = []

    while i < limit:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + increment 
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "
    for num in numbers:
        print num

while_loop(6, 1)