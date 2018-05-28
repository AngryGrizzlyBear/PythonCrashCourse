# This is more or less a review on Variables

message = "Hello World! I'm pretty hungry for a burrito.\n"
print(message)

message = "Now I need to go get something to eat!\n"
print(message)

name = "ada lovelace'\n"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

print(full_name.title())

print("Hello, " + full_name.title() + "!")

message = "Hello, " + full_name.title() + "!"
print(message)

print("Languages:\n\tPython\n\tC\n\tJavascript")


# 2-3
print ("Hello person. What a lovely evening this is.")

# 2-4
first_name = "jon"
last_name = "smith"
full_name = first_name + " " + last_name
print(full_name.title())
print(full_name.lower())
print(full_name.upper())

# 2-5
print('''Kevin Hart said "Everybody wants to be famous, but nobody wants to do the work. 
                          I live by that. You grind hard so you can play hard."
''')

famous_person = "Marco Rubio"
famous_quote = """
                'The American Dream is a term that is often used but also often misunderstood. 
                It isn't really about becoming rich or famous. It is about things much simpler 
                and more fundamental than that.'
               """
print(famous_person + " said" + famous_quote)