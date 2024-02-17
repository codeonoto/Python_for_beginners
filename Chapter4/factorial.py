n = int(input("Enter n:"))


def factorial(n):
    ans = 1
    if n == 0:
        ans = 1
    else:
        for i in range(1, n + 1):
            ans *= i

    return ans


output = factorial(n)
print("THe factorial is:", output)
