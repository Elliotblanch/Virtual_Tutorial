print("Hello World")

#Setting variables from terminal
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")

print ("Hello " + first_name + " " + last_name)


age = input("Please enter your age: ")
defAge = int(age)

time = input("What time is it?")
defTime = float(time)

tired = input("True or False: are you tired?")
defTired = bool(tired)

print (f"{first_name} is {age} years old")

print (f"{first_name} will be {defAge+10} years old in a decade")

print(f"Statement: it is {time} & tired = {defTired}")