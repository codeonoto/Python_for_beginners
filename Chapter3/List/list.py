# List Items
# Indexed
# Ordered
# Mutable
# Duplicates Allowed
# Any Datatype
# Mix of different data type

# Creating a list 
fruits = ["apple", "mango", "cherry", "banana"]

# Printing a list 
print(fruits) 

# Check type of list 
print(type(fruits))

# Check length of list
print(len(fruits))

# Checking if an item is present in the list 
if "banana" in fruits:
    print("Banana is part of the list")
    
# Checking if an item is not present in the list 
if "kiwi" not in fruits:
    print("Kiwi is not a part of the list")
    
# Indexing in list
print(fruits[1])
print(fruits[1:3])

# Negative Indexing in list
print(fruits[-3])
print(fruits[-3:-1])
