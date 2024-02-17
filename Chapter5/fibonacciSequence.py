def fibonacci(n):

    # Base Case
    if n == 1:
        return 0
    elif n == 2:
        return 1

    # Recursive Case:
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Enter the value of n:"))

for i in range(1, n + 1):
    print(fibonacci(i), end="->")
