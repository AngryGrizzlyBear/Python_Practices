# This is a function, and we make the paramiters here.)
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"
# We're printing a string here, while calling the function, directly giving it numbers.
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)
# We created a set of variables here, just to call them later in the function in cheese_and_crackers. cheese_and_crackers(amount_of_cheese(10), amount_of_crackers(50))
print "Or, we can use variables from our script:"

amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)
# This is printing a string, followed by calling the function cheese_and_crackers, adding two numbers together, one on each break.)
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)
# This part is printing a string, followed by calling cheese_and_crackers, adding a varriable + a number, with another variable adding to another number.)
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def collection_of_games(old_games, new_games, total_games):
    print "You own %d old games." % old_games
    print "You own %d new games" % new_games
    print "Total, you have %d games combined.\n" % total_games

old_games = 10
new_games = 40
total_games = old_games + new_games


collection_of_games(old_games, new_games, total_games)

print "Let's try a different count on your library."
collection_of_games(100, 30, 100 + 30)

print "I liked how that work. Can we add it a different way? We can!"
collection_of_games(10 + 20, 34+20, 200+1000)

print "What about this way?"
collection_of_games(20, 30, 40)