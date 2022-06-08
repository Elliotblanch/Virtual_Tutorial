name = "Elliot,John,Blanchfield"

#str.lower()    converts string to lowercase
print(name.lower())
#str.upper()    converts string to uppercase
print(name.upper())
#str.replace    replaces old substring with new one 
print (name.replace("Elliot","Peregrin"))
#str.split()    returns a list of words in the string
#we can specify the seperator inside the parenthesis
print(name.split(","))
#str.join       concatenates an iterable or collection of strings
print(" join ".join(["Elliot", "John", "Blanchfield"]))
#str.count()    returns a number of non overlapping occurances of substring in string
#this is case sensitive
print(name.count("l"))
#str.isdigit()  returns true if string is a digital string
str1 = "Cat"    # Returns false
str2 = "123"    # Returns true
str3 = "12.34"  # Returns false

print(str1.isdigit())
print(str2.isdigit())
print(str3.isdigit())

#concatination  combining strings together
print("cat" + "dog") # Returns catdog
print("cat" , "dog") # Returns cat dog

school = "High"
age = 15
maths = True
testscore = 75.5

print("My name is", name, "My age is", age, "maths:", maths, "I scored", testscore, "on the test")

#f stromgs allow is to combine multiple datatypes in a string
# as well as perform calculations within curly brackets

print(f'My name is {name} My age is {age+11} maths: {maths} I scored {testscore-27} on the test')

#\" allows you to enter "" without it being considered syntax
print("Hello my name is \"Elliot\"")
# \n starts a new line
print("Hello \nmy name is Elliot")
# \t presses tab
print("Hello \tmy name is Elliot")
