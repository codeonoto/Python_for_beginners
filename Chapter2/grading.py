percentage = float(input("Enter Your Percentage : "))

if (percentage >= 81 and percentage <= 100):
    print("Very Good")
    
elif (percentage >= 61 and percentage <= 80):
    print("Good")
    
elif (percentage >= 41 and percentage <= 60):
    print("Average")
    
elif (percentage <= 40):
    print("Fail")
    
else:
    print("Enter a Valid Number")