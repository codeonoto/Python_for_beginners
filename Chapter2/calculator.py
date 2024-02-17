num1 = int(input("Enter Number 1 : "))
num2 = int(input("Enter Number 2 : "))

operator = input("Enter Operator (+,-,*,/): ")

match operator:
    case "+":
        print("Sum is : ", num1 + num2 )
    
    case "-":
        print("Difference is : ", num1 - num2)
        
    case "*":
        print("Product is : ", num1 * num2)

    case "/":
        print("Division is : ", num1 / num2)

    case _ :
        print("Enter a valid operator")