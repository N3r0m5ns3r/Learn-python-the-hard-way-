# create a mapping of state of abbrev
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CL',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CL': 'Los Angeles',
    'MI': 'Detroit',
    'FL': 'Tampa'
}
# add more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out the cities
print('-' * 10)
print("NY state has: ", cities['NY'])
print("OR states has: ", cities['OR'])

# print some states
print('-' * 10)
print("Michingan's abbrev is: ", states['Michigan'])
print("Florida's abbrev is: ", states['Florida'])

# do it by using the state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every abbrev
print('-' * 10)
for state, abbrev in list(cities.items()):
    print(f"{state} is abbrev {abbrev}")

# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")


print('-' * 10)
#safely get a abbrev by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry, No tehas")

# get a city with a deflt value
city = cities.get('TX', 'Does not exist')
print(f"the city for the state 'TX' is: {city}")
