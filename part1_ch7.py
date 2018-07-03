# How the input function works
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

name = input("Please enter your name: ")
print("Hello, " + name + "!")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")

# Using int to Accept Numerical Input
age = input("How old are you? ")
print("\n You are " + age + " years old!")
age = int(age)
print(age >= 18)

# rollercoaster
height = input("How tall are you in inches? ")
height = int(height)
if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

# Modulo

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")

# 7-1 Exerise rent a car
car = input("What kind of car would you like to rent?: ")
print("Let me see if I can find you a " + car + ".")

# 7-2 Resturant Seating

seating = input("How many people are in your dinner group?: ")
seating = int(seating)
if seating >= 8:
    print("\nYou will have to wait for a table.")
else:
    print("\nWe have more than enough for your group!")