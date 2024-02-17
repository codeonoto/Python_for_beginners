def sum_1_to_N(n):
    if n == 1:
        return 1
    
    sum = n + sum_1_to_N(n-1)

    return(sum)

n = int(input("Enter the value of n:"))
print(sum_1_to_N(n))
