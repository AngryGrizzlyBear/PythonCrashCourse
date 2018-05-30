# Lists
bicycles = ['trek', 'cannodale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1].title())
print(bicycles[3].title())
print(bicycles[-1].title())

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

# 3-1
name = ["Kermmit", "Shawn", "Steve", "Nathan"]

#3-2
message = "Hello, " + name[2].title() + "."
print(message)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# or

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

motorcycles = []

motorcycles.append('toyota')
motorcycles.append('suzuki')
motorcycles.append('harley')

print(motorcycles)

# insert
motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, 'ducati')
print(motorcycles)

# del
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[1]
print(motorcycles)

# pop

motorcycles = ['honda1', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0)
print('The first motorcyle I owned was a ' + first_owned.title() + '.')

# remove

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

# 3-4 Guest List
guest_list = ['Sandra', 'Chris', 'Stephen', 'Mary']
print("\n" + guest_list[0] + ", You have been invited to my party!")
print("\n" + guest_list[3] + ", You are most welcome to come to enjou the festivities.")
print("\n" + guest_list[1] + ", You can bring yourself and your mother to my party")
print("\n" + guest_list[2] + ", You can wear any type of shoes for my party! You're invited!")