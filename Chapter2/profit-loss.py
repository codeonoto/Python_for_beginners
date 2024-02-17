cp = int(input("Enter the Cost Price : "))
sp = int(input("Enter the Selling Price : "))

if (sp > cp):
    profit = sp - cp
    print("You got a Profit of ", profit)

elif sp < cp:
    loss = cp - sp
    print("You got a Loss of ", loss)

else:
    print("NO PROFIT NO LOSS")