##### method 1 #####

digit = int(input("enter your number :"))

count = 0

if digit == 0:
    count = 1
    
else:
    while digit > 0:
        count += 1
        digit //= 10
        
print(f"total number of digit is {count}")



###### mehod 2#######

num = int(input("enter your number"))

count = abs(len(str(num)))
print("total digit is", count)


###### method 3 ######


num = str(abs(int(input("enter your digit:"))))

count = 0

for _ in num:
    count += 1
    
print(count)