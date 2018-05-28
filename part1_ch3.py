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