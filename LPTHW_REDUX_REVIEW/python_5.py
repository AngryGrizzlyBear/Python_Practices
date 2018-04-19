my_name = 'Zed A. Shaw'
my_age = 35
my_height = 74 * 2.54
my_weight = 180 * 0.453592
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name  
print "He's %d cm tall." % my_height
print "He's %d kilos heavy." % my_weight
print "Actually, that's not too heavy."
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)
