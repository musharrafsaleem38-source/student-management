# age = 39
# print(age, type(age))
# jh = "g"
# print(type(jh))
# jhi = True
# print(type(jhi))
# fgh = {"as":87}
# print(type(fgh))
# pi = 3.14
# print(type(pi))
# x = 5
# y = 2
# print(bin(y<<3))
# 8
# jfh = [65, 19, 2400102786, 375]
# jfh.sort()
# print(jfh)

# x= int(input("h"))
# y=x/2
# print(int(y))

# import random


# value = random.randint(1,10)
# attempt = 0


# while attempt<7:
#     num = int(input("enter your geussing no."))
    
    
#     if value == num:
#         print("you guess the correct ")
#         break
#     else:
#         print("ry again")
        
#     attempt +=1
    
# print(value)

# marks = int(input("enter your marks"))

# if marks >= 90:
#     print("you got A grade",marks)
    
# elif marks >=80 and marks <90:
#     print("you got grade B", marks)
    
# elif marks >=70 and marks <80:
#     print("you got grade C")
    
# else:
#     print("you failed in exam")

# password = input("Enter your password: ")

# if not password[0].isupper():
#     print("First letter must be capital")bbe

# elif not any(ch.isdigit() for ch in password):
#     print("Password must contain at least one digit")

# elif password.isalnum():
#     print("Password must contain at least one special character")

# else:
#     print("Your password is successfully generated:", password)

# contact = {}
# while True:
#     name = input("enter your name:")
#     number = int(input("enter your number:"))
#     contact[name] = number
    
#     add = input("you want to add more contact'yes/no'")
#     if add.lower == "no":
#         break

# search = input("ener name:")

# if search in contact:
#     print("funnd", contact[name])
# else:
#     print("not found")



# balance = int(input("enter your balance:"))


# while True:
#     print("1. check balance")
#     print("2. withraw")
#     print("3. deposit")
#     print("4. exit")
    
#     choice = int(input("inter your choice:"))
    
#     if choice == 1:
#         print("your current balance is", balance)
#         break
        
#     if choice == 2:
#         amount = int(input("enter the amoumt: "))
        
#         current = (balance - amount)
#         print("your current balance is", current)
#         break
        
#     if choice == 3:
#         amount = int(input("enter the amoumt: "))
        
#         current = (balance + amount)
#         print("your current balance is", current)
#         break
        
#     if choice >= 4:
#         print("please enter valid choice")
#         break


# import time

# alarm = input("set your alarm-")

# while True:

#     current = time.strftime("%H:%M:%S")
    
#     if current == alarm:
#         print("alarm ringing")
#         break
    
#     time.sleep(2)

# import time
# from playsound import playsound

# alarm = input("Set alarm (HH:MM:SS): ")

# print("Alarm set...")

# while True:
#     current = time.strftime("%H:%M:%S")

#     if current == alarm:
#         print("Alarm ringing!")
#         playsound("C:\\phone\\audio\\Tearful Emotional Track 2022 _ Ab yad Na Aao ....mp3")    # your sound file
#         break

    # time.sleep(1)
    
# import time
# from playsound import playsound

# alarm = input("Set alarm (HH:MM:SS): ")

# print("Alarm set...")

# while True:
#     current = time.strftime("%H:%M:%S")

#     if current == alarm:
#         print("Alarm ringing!")
#         playsound("C:\\phone\\audio\yaad na aao.mp3.mp3")
#         break

#     time.sleep(1)




# word = input("write a string: ")
# rev = ""

# for i in word:
#     rev = i + rev
    

# print(rev)


class Parent:
    def m1(self):
        print("Hello")

class Child(Parent):
    def m2(self):
        print("Good byee ..... ")

ch = Child()
# ch.sayhello()
# ch.say_goodbye()

ch.m2()
ch.m1()