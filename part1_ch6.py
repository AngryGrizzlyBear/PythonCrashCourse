# a simple dictionary
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

# Working with Dictionaries
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

# Adding new key-value pairs

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Starting with an Empty Dictionary
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

# Modifying Values in a Dictionary

alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))

# Move the alien to the right
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))

# Removing Key Value Pair
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

# A dictionary of similar objects

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")

# Try it yourself. 6-1

person = {
    'first_name': 'stephen',
    'last_name': 'stark',
    'age': 82,
    'city': 'tupacsville'
}
print(person['first_name'].title())
print(person['last_name'].title())
print(person['age'])
print(person['city'].title())

# 6-2 exercise
favorite_numbers = {
    'mark': 23,
    'steven': 33,
    'erik': 53,
    'mavis': 92,
    'nana': 82,
}

num = favorite_numbers['mark']
print("Mark's favorite number is " + str(num) + ".")
num = favorite_numbers['steven']
print("Steven's favorite number is " + str(num) + ".")
num = favorite_numbers['erik']
print("Erik's favorite number is " + str(num) + ".")
num = favorite_numbers['mavis']
print("Mavis's favorite number is " + str(num) + ".")
num = favorite_numbers['nana']
print("Nana's favorite number is " + str(num) + ".")

# 6-3

glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at at time',
    'dictionary': 'A collection of key-value pairs',
}

word = 'string'
print("\n" + word.title() + ": " + glossary[word])

word = 'comment'
print("\n" + word.title() + ": " + glossary[word])

word = 'list'
print("\n" + word.title() + ": " + glossary[word])

word = 'loop'
print("\n" + word.title() + ": " + glossary[word])

word = 'dictionary'
print("\n" + word.title() + ": " + glossary[word])

# Testing something
for key, value in glossary.items():
    print("\nKey: " + key)
    print("Value: " + value)

# Looping through a dictionary

# Looping through all key values

user_0 = {
    'username': 'efermi',
    'fisrt': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

print("\n˚")

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + '.')

for name in favorite_languages.keys():
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() +
        ", I see your favorite language is " +
        favorite_languages[name].title() + "!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# Looping through a Dictionary's Key in order

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

# Looping through all values in a dictionary

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# 6-4
print("\n This begins the next segment.")

glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at at time',
    'dictionary': 'A collection of key-value pairs',
    'key': 'The first item in a key-value pair in a dictionary.',
    'value': 'An item associated with a key in a dictionary.',
    'conditional test': 'A comparison between two values',
    'float': 'A numerical value with a decimal component.',
    'boolean expression': 'An expression that evaluates to True or False.',
}

for word, definition in glossary.items():
    print("\n" + word.title() + ": " + definition)

# 6-5
print("'\n This is the enext segment.")

rivers = {'nile': 'egypt',
          'mississipi': 'united states',
          'fraser': 'canada',
          'kuskokwim': 'alaska',
          'yangtze': 'china',}

for river, country in rivers.items():
    print("The " + river.title() + " flows through " + country.title() + ".")

print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print("- " + river.title())

print("\nThe following countries are included in this data set:")
for country in rivers.values():
    print("- " + country.title())

# 6-6

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

print("\n")

coders = ['phil', 'josh', 'david', 'becca', 'sarah', 'matt', 'danielle']
for coder in coders:
    if coder in favorite_languages.keys():
        print("Thank you for taking the poll, " + coder.title() + "!")
    else:
        print(coder.title() + ", what's your favorite programming language?")

print("\n")
# Nesting

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

aliens = []

# make 30 green aliens

for alien in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] == 'yellow'
        alien['speed'] == 'medium'
        alien['points'] = 10
# Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))

print("\n")

# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

# Summarize the order
print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

#6-7
print("\nThis is the next segment")

# Make an empty list to store people in.
people = []

# Define some people, and add them to the list.
person = {
    'first_name': 'eric',
    'last_name': 'matthes',
    'age': 43,
    'city': 'sitka',
}

people.append(person)

person = {
    'first_name': 'ever',
    'last_name': 'matthes',
    'age': 5,
    'city': 'sitka',
}

people.append(person)

person = {
    'first_name': 'wilie',
    'last_name': 'matthes',
    'age': 8,
    'city': 'sitka',
}

people.append(person)

# Display all of the information in the dictionary.
for person in people:
    name = person['first_name'].title() + person['last_name'].title()
    age = str(person['age'])
    city = person['city'].title()

    print(name + ", of " + city + ", is " + age + " years old.")

# 6-8 Pets
# Make an empty list tos tore the pets in.
pets = []

# Make individual pets, and store each one in the list.
pet = {
    'animal': 'python',
    'name': 'john',
    'owner': 'guido',
    'weight': 43,
    'eats': 'bugs',
}

pets.append(pet)

pet = {
     'animal type': 'chicken',
    'name': 'clarence',
    'owner': 'tiffany',
    'weight': 2,
    'eats': 'seeds',
}

pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'pesto',
    'owner': 'eric',
    'weight': 37,
    'eats': 'shoes',
}

pets.append(pet)

# Display information about each pet.
for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ': ' + str(value))

# 6- 9
favorite_places = {
    'eric': ['bear mountain', 'death valley', 'tierra del fuego'],
    'erin': ['hawaii', 'iceland'],
    'ever': ['mt. verstovia', 'the playground', 'south carolina']
}

for name, places in favorite_places.items():
    print("\n" + name.title() + " likes the following places:")
    for place in places:
        print("- " + place.title())

#6-10 Favorite Numbers

favorite_numbers = {
    'mandy': [42, 17],
    'micah': [42, 39, 56],
    'gus': [7, 12]
}

for name, numbers in favorite_numbers.items():
    print("\n" + name.title() + " likes the following numbers:")
    for number in numbers:
        print(" " + str(number))