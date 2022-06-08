age = int (input("What's your age: "))
if age >= 85:
    print("85 or older")
elif age >= 65:
    print("Age between 65 & 85")
elif age >= 45:
    print("Age between 45 & 65")
elif age >= 25:
    print("Age between 25 & 45")
elif age >= 18:
    print("Age between 18 & 25")
else:
    print("Under 18")