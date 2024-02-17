# Pass by reference and Pass by value

# 1) Pass by value : (Immutable objects - strings, integers, float, tuples)
#  when passed to function, a copy of the object is created
#  & assigned to loacl variable in function
#  Any change made to them in side function, not affect the original variable

print("PASS BY VALUE")
x = 5


def addOne(x):
    x = x + 1
    print("Inside function:", x)


addOne(x)
print("Outside Function:", x)


# 2) Pass by Reference : (Mutable objects - list, dict)
#  A reference to actual object is passed to function
# changes inside the function will affect the original object

print("\nPASS BY REFERENCE")

list = [1, 2, 3]


def modifyList(list):
    list.append(4)
    print("Inside Function :", list)


modifyList(list)

print("Outside function: ", list)
