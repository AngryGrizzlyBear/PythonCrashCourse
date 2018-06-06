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

registered_players = ['Thomas', 'Sebastian', 'Christina']
not_registered_players = 'Sam'

if not_registered_players not in registered_players:
    print(not_registered_players.title() + ", You need to register to play this game.")

for player in registered_players:
    print(player + ', welcome to the game!')

# Simple if statements: Voting
age = 18
if age >= 18:
    print("\nYou are old enough to vote!")
    print("Have you registered to vote yet?")
elif age >= 17:
    print("\nYou definitely need to vote.")
else:
    print("\nYou're not old enough to vote.")
    print("Please register to vote as soon as you turn 18!")

# Amusement Park
age = 20

if age < 4:
    print("Your admission costs $0.")
elif age < 18:
    print("Your admission costs $5.")
else:
    print("Your admission costs $10.")

age = 65

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 10

print("Your admission cost is $" + str(price) + ".")

# Testing multiple conditions
print("\n")
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")


#5-3 Alien Colors 1

alien_color = 'red'
if alien_color == 'green':
    print("You've earned 5 points!")

# 5-4 Alien Colors 2
else:
    print("You've earned 10 points!")

# 5-5 Alien Colors 3

alien_color = 'red'
if alien_color == 'green':
    print("\nYou've earned 5 points!")
elif alien_color == 'yellow':
    print("\nYou've earned 10 points!")
else:
    print("\nYou've earned 15 points!")

# 5-6 Stage of Life

age = 83

if age < 2:
    life = 'baby'
elif age < 4:
    life = 'toddler'
elif age < 13:
    life = 'kid'
elif age < 20:
    life = 'teenager'
elif age < 65:
    life = 'adult'
else:
     life = 'elder'
print("You're just a " + life + ".")

# 5-7 Favorite Fruit

favorite_fruit = ['bananas', 'green apples', 'pineapples']

if 'bananas' in favorite_fruit:
    print("\nYou really like bananas!")
if 'green apples' in favorite_fruit:
    print("You really like green apples!")
if 'pineapples' in favorite_fruit:
    print("You really like pineapples!")
if 'kiwi' in favorite_fruit:
    print("You really like kiwis!")
if 'strawberries' in favorite_fruit:
    print("You really like strawberries!")
