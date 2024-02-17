# function --> blocks of reusable code that perform a specific task.

n = int(input("Enter any number : "))


def printHello():
    print("Hello World")


def sumOneToN(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum


output = sumOneToN(n)


printHello()
print("Sum of all numbers till n is : ", output)
