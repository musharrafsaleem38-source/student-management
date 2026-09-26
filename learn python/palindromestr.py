string = input("enter your string :")

temp = string

rev = string[ : :-1]

if rev == temp:
    print(f"{string} is palindrome")
    
else:
    print(f"{string} are not palindrome")