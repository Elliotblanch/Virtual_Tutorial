list1= ["red", "green", "blue", "yellow", "purple"]

# We can reference list elements using an index number, starting at 0
print(list1[1])
# We can reference the last element with [-1]
print(list1[-1])
# We can slice the list into smaller sections by using [x:y]
print(list1[1:3])
# If we do not include the stopping point, it will return all values from that point on
print(list1[1:])

# We can cahnge the element in a list by setting a new value to the list index
list1[1] = "pink"
print(list1)

# To delete an element from a list we use the del keyword & the index of the item we wish to delete
del list1[-1]
print(list1)

# We can check if an element is/is not in a list
print("blue" in list1)
print("blue" not in list1)

print("=================")

lista = ["sport", "comedy", "drama"]
listb = ["dog", "cat", "mouse"]
listc = [33, "word", 143]
listlist = [lista, listb, listc, 127, 33.3]

## Prints the second element from list a
print(listlist[0][1]) # Returns Comedy
