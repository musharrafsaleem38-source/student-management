num = int(input("enter your number :"))

original = num
reverse = 0

while num>0:
    digit = num % 10
    reverse = reverse *10 + digit
    num //= 10
    
if original == reverse:
    print("this is a pallindrome")
    
else:
    print("this is not pallindrome")