fruits = ["apple", "mango", "cherry", "banana"]

# append() --> add item to the end of the list
fruits.append("kiwi")
print(fruits)

# insert() --> insert the element at given place
fruits.insert(1, "strawbeery")
print(fruits)

# extend() --> adding another list 
more_fruits = ["tomato", "watermelon"]
fruits.extend(more_fruits)
print(fruits)

# + operator
new_fruits = fruits + more_fruits
print(new_fruits)