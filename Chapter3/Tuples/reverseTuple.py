input_tuples = (1,2,3,4,5,6)

list = []

# Add Reversed Values in a list
for x in reversed(input_tuples):
    list.append(x)
    
# TypeCast into tuple
output_tuple = tuple(list) 
print(output_tuple)