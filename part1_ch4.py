# Part 1 Example 1.

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title())

# Doing more with a for loop

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print("\n" + magician.title() + ", you did a fantastic trick!")

# Doing even more with a for loop

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print("\n" + magician.title() + ", you did a fantastic trick!")
    print("Can't wait to see your next trick, " + magician.title() + "!\n")

print("Thank you everyone! That was a wonderful performance! Great magic show!")

# 4-1 Exercise Review
pizzas = ['Meat Lovers', 'Hawaiian', 'Pepperoni']
for pizza in pizzas:
    print("\nI like " + pizza.title() + " pizza!")

print("\nI really love these topings. These topings make pizza taste ten times"
      " better! I really like pizza!")

doggo = ['Akita', 'Shiba Inu', 'Malamute']
for dog in doggo:
    print("\nA " + dog.title() + " would make a really great pet!")

print("\nThese are really great dogs!")

# Using the range function
for value in range(1,5):
    print("\n")
    print(value)

for value in range(1,6):
    print("\n")
    print(value)

# Using range to Make a List of Numbers
numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)

print(squares)

# clener version
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

# Simple statistics with a List of Numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

# List Comprehensions
square = [value**2 for value in range(1,11)]
print(squares)

# 4-3 Exercise Counting to Twenty

counting = range(1,21)
for count in counting:
    print(count)

# 4-4 One Million
numbers = range(1, 100000001)
#for number in numbers:
 #   print(number)

# 4-5 Min, Max Sum
print(max(numbers))
print(min(numbers))
print(sum(numbers))

# 4-6 Odd Numbers
more_numbers = list(range(1,21,4))
for num in more_numbers:
    print(num)
print("\nNew Space")
# 4-8 Threes

cubes = []
for number in range(1, 11):
    cube = number**3
    cubes.append(cube)

for cube in cubes:
    print(cube)

# 4-9

cubes = [number**3 for number in range(1, 11)]

for cube in cubes:
    print(cube)

# Slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# More Slice Practice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])

# Even more slicing
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])

# More slciing examples
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])

# Even more
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])

# Looping through a slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# Copying a List
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("my favorite foods are:")
print(my_foods)

print("\nMy Friend's faborite foods are:")
print(friend_foods)

# adding to the list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("my favorite foods are:")
print(my_foods)

print("\nMy Friend's faborite foods are:")
print(friend_foods)

# 4-10 Slices
fruits = ['apple', 'orange', 'pears', 'grapefruit', 'grapes', 'strawberries']
print('\nThe first three items in the list are:')
for fruit in fruits[:3]:
    print(fruit.title())

print('\nThe middle items in the list are:')
for fruit in fruits[1:5]:
    print(fruit.title())

print('\nThe last three items in the list are:')
for fruit in fruits[2:6]:
    print(fruit.title())

# new pizza list
good_pizzas = ['Meat Lovers', 'Hawaiian', 'Pepperoni', 'Sausage']
friend_pizza = good_pizzas[:]

good_pizzas.append('olives')
friend_pizza.append('chicken')

print("\nI like these topings:")
for pizza in good_pizzas:
    print(pizza)

print("\nMy friend likes these topings:")
for pizza in friend_pizza:
    print(pizza)

# Tuple
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
print("\n")

# Looping through the values
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

# Writing over a Tuple
dimensions = (200, 50)
print("Original Dimensions:")
for dimension in dimensions:
    print(dimension)


dimensions = (400, 100)
print("\nModified Dimensions:")
for dimension in dimensions:
    print(dimension)

print("\n")

# 4-13 Buffet
buffet_foods = ('beef', 'chicken', 'steak', 'vegetarian', 'soup')
print("You can choose from the following options on our menu:")
for food in buffet_foods:
    print(food.title())

buffet_foods = ('beef', 'chicken', 'steak', 'ham sandwhich', 'turkey')
print("\nWe have updated our menu. Please see the following:")
for food in buffet_foods:
    print(food.title())