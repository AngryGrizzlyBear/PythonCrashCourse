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

# 3-5 Changing Guest List

print("\nLooks like " + guest_list[2] + " can't make it. That's too bad. Take him off the list.")
guest_list.remove('Stephen')
print("\nThere, he's gone! Invite someone else to replace him.")
guest_list.insert(2, 'Samantha')
print("\nStephen has been replaced by " + guest_list[2] + ". You are now invited to my party.")
print("\n" + guest_list[0] + ", " + guest_list[1] + ", and " + guest_list[3] + " are all still welcomed to my party.")
print("\nPlease resend them inviations, as well as an invitation to Samantha.")

# 3-6 More Guest

print("\n" + guest_list[0] + ", " + guest_list[1] + ", " + guest_list[2] + ", and " + guest_list[3] +
      " should be informed that I have found a larger table. Please inform them of the change. I will be adding"
      " three more guest to the party!")

guest_list.insert(0, 'Thomas')
print('\n' + guest_list[0] + " will be added to the party, please send him an invitation.")

guest_list.insert(2, 'William')
print('\n' + guest_list[2] + " will be added to the party, please send him an invitation." )

guest_list.append('Sophie')
print('\n' + guest_list[6] + " woll be added to the party, please notify her at once.")

# getting ready to pop some names off of the list.
print("\nUh-oh. Looks like we won't be able to get that dinner reseveration. Time to remove some people"
      " off of the list!")
guest_list.pop()