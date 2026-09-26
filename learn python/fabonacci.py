num  = int(input("enter your number :"))

a=0
b=1

print("fabonacci serries : ")

for i in range(num):
    print(a, end = ' ')
    
    c= a+b
    a=b
    b=c