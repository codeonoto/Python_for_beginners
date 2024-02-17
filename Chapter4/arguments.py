# def add(n1, n2=0):
#     print("n1 :",n1)
#     print("n2 :",n2)
#     sum = n1 + n2
#     return sum

# # Positional Argument
# print("The sum is ", add(2, 3))

# # Keyword agrument (named arguments)
# print("The sum is ", add(n1=3, n2=2))

# # Defualt Arguments
# print("The sum is ", add(3))

# Arbitary arguments (variable-length arguments *args and **kwargs)

# *args --> tuples
# def addAllNumbers(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum


# output = addAllNumbers(2, 3, 4, 5)
# print(output)

# **kwargs --> keyworded arguments / key-value pair arguments
# as a dict.

def studentInfo(**kwargs):
    for x,y in kwargs.items():
        print(x,y)
        
studentInfo(name="SBlock", age=20, city="Bhopal")
studentInfo(name="SBlock", age=20, city="Bhopal")
studentInfo(name="SBlock", age=20, city="Bhopal")

