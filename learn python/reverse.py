num = int(input("enter your number:"))

reverse = 0

while num>0:
    digit = num %10
    reverse = reverse * 10 + digit
    num //=10
    
print(f"after reverse the number is {reverse}")