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