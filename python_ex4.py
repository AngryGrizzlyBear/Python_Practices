cars = 100
# Changing space_in_car to 4 instead of 4.0 ultimately changes carpool_capacity. The original answer is 120.0, but is soon changes to 120.
# = assigns the value on the right to a variable on the left. == tests if two things have the same value, which is covered in exercises 27.
# _ is an underscore character that we use as a placeholder to fill in for spaces.
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
