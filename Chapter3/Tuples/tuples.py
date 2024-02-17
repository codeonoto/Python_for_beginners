# Tuplse --> used to store multiple items in a variable
# colors = ("blue", "green", "red")

# Properites
# Ordered
# Immutable
# Duplicates
# Any Datatype
# Mix of diffrerent data types

# Creating a Tuple
colors = ("blue", "green", "red")

# Check type of tuple
print(type(colors))

# Check length
print(len(colors))

# Accessing items in tuple
print(colors[0])
print(colors[-3])

print(colors[0:2])

# Check if an item exist in tuple
if "green" in colors:
    print('Green Color is in stock!')

if "pink" not in colors:
    print('Pink color is out of stock')


# Traverse the tuple
for i in colors:
    print(i)
    
    
# Concatenate 2 tuples
more_colors = ("pink", "black")
new_colors = colors + more_colors
print(new_colors)

# Unpacking of Tuple
color1, color2, color3 = colors
print(color1, color2, color3)