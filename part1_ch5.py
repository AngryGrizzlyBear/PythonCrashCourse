# A simple example

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Checking for Inequality

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

# Numbers

answer = 17

if answer != 42:
    print("That is not the correct answer. Please try again!")

# Checking whether a value is not in a list
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

# Boolean Expression

game_active = True
can_edit = False

# 5 - 1 Conditional Tests
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car = 'audi? I predict False.")
print(car == 'audi')

requested_car = 'jeep'
if requested_car != 'bmw':
    print("\nI don't want that car!")
    print(requested_car == 'bmw')

new_car = 'toyota'
print(new_car.lower() == 'toyota')

age_limit = 21
age_zero = 23
age_one = 24
if age_zero and age_one >= age_limit:
    print("You're old enough to get in.")
if age_zero or age_one == age_limit:
    print("Huh? This doesn't make any sense.")
