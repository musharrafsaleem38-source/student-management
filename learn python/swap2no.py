num1 = int(input("enter 1st no. : "))
num2 = int(input("enter 2nd no. : "))

print("before swaping ")
print(f"num1 = {num1} and num2 = {num2}")

print("after swaping :")

num1 = num1 + num2 
num2 = num1 - num2
num1 = num1 - num2

print(f"num1 = {num1} and num2 = {num2}")