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

#4-3 Exercise Counting to Twenty

counting = range(1,21)
for count in counting:
    print(count)