def printNum(n):
    
    if n == 0:
        return 1
    
    print(n)
    printNum(n-1)

n = int(input("Enter the value of n:"))
printNum(n)