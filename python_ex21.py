def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract (78, 4)
weight = multiply(90, 2)
iq = divide(100,2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
# what = add(age(30, 5) subtract(a, b)(height(78 -4) multiplay(a, b)(weight(90 *2), divide(a / b))))
# what = add(age, subtract(height, multiply(weight, divide(iq(100,2), 2))))
# what = add(age, subtract(height, multiply(weight, divide(50, 2))))
# what = add(age, subtract(height, multiply(180, divide(50, 2))))
# what = add(age, subtract(74, multiply(180, 25)))
# what = add(age, subtract(74, 4500))
# what = add(35, subtract(74, 4500))
# what = add(35, -4426)
# what = - 4391

print "That becomes: ", what, "Can you do it by hand?"

what_2 = 5 + add(age, subtract(23, multiply(24, divide(weight, 2))))

print "That's: ", what_2, "Yee."