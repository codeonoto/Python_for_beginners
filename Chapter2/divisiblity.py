num = int(input("Enter a positive number : "))

if (num % 4 == 0):
    if (num % 5 == 0):
        if(num % 15 == 0):
            print("not valid number")
        else:
            print("Number is Valid")
            
else: 
    print("Not a Valid Number")