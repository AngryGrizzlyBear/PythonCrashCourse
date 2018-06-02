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