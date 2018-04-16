from sys import argv
script, from_file, to_file = argv

print "Copying from %s to %s. Ok, done." % (from_file, to_file)

# Got this one down to one line.
indata = open(from_file).read()

out_file = open(to_file, 'w')
out_file.write(indata)

out_file.close()
