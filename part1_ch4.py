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
