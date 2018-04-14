from sys import argv

script, filename = argv
# This will instead read the file instead of writing the file. 
target = open(filename, 'r')
# I should've reviewed my last notes to try to make this make sense. He did go over this in the last chapter, so this is pretty solid.
print target.read()