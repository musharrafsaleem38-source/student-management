num1 = int(input("enter your 1st number : "))
num2 = int(input("enter your 2nd number : "))
num3 = int(input("enter your 3rd number : "))

if(num1>num2 and num1>num3):
    print("num1 is greater")
    
if(num2>num1 and num2>num3):
    print("num2 is greatest" , num2)
    
if(num3>num1 and num3>num2):
    print("num3 is greatest")