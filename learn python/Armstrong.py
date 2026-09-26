num = int(input("Enter a number: "))

temp = num
digits = len(str(num))
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** digits
    temp //= 10

if total == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
    
