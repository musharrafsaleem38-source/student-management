num = int(input("enter your number :"))

if(num<=1):
    print("not prime number")

for i in range(2,num):
    if num % i == 0:
        print(f"{num} is not the prime number")
        break
else:
    print(f"{num} is the prime number")
    