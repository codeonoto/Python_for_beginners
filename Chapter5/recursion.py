def factorial(n):

    # Base Case
    if n == 0:
        return 1

    # Recursive Case
    ans = n * factorial(n - 1)
    return ans


n = int(input("Enter the value of n:"))
print(factorial(n))
