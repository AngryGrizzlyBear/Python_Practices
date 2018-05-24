states = {
    'Washington': 'WA',
    'Wyoming': 'WY' ,
    'Nevada': 'NV',
    'Montana': 'MT'
}

cities = {
    'WA': 'Seattle',
    'NV': 'Carson City',
    'MT': 'Helena'
}

cities['WY'] = 'Cheyenne'

print '-' * 10
print "WY State has: ", cities['WY']

print '-' * 10
print "Nevada's abbreviated state is: ", states['Nevada']
print "Montana's abbreviated state is: ", states['Montana']

print '-' * 10
print "Washington has: ", cities[states["Washington"]]
print "Nevada has: ", cities[states["Nevada"]]


